import json
import logging
from typing import Generator, Set

from scrapy import Request
from scrapy.http.response import Response
from scrapy.loader import ItemLoader
from scrapy.spiders import SitemapSpider

from McDonalds.items import McDonaldsItem


class scrapeMcDonalds(SitemapSpider):  # type: ignore
    name = "scrapeMcDonalds"
    allowed_domains = ["mcdonalds.com"]
    sitemap_urls = ["https://www.mcdonalds.com/us/en-us/sitemap.xml"]
    sitemap_rules = [("/us/en-us/product/", "parse")]
    visitedItemIds: Set[str] = set()

    def __init__(self) -> None:
        SitemapSpider.__init__(self)
        rootLogger = logging.getLogger()
        rootLogger.setLevel(logging.DEBUG)

        logFormatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s")

        # file handler
        fileHandler = logging.FileHandler("Output.log")
        fileHandler.setLevel(logging.DEBUG)
        fileHandler.setFormatter(logFormatter)
        rootLogger.addHandler(fileHandler)

        # console handler
        consoleHandler = logging.StreamHandler()
        consoleHandler.setLevel(logging.DEBUG)
        consoleHandler.setFormatter(logFormatter)
        rootLogger.addHandler(consoleHandler)

    def parse(self, response: Response) -> Generator[Response, None, None]:
        # Find the item ID and then make a request for the item details.
        itemId = response.css("div.itemID::attr(data-item-id)").extract()
        itemDetailUrl = f"https://www.mcdonalds.com/wws/json/getItemDetails.htm?country=US&language=en&showLiveData=true&item={itemId[0]}"  # noqa: E501
        yield Request(
            itemDetailUrl, method="GET", callback=self.parse_details
        )  # meta={'visitedItemId': visitedItemId})

    def parse_details(self, response: Response) -> Generator[Response, None, None]:
        # Parse the item detail response
        dailyValue = {
            "calories": 0,
            "calories_from_fat": 0,
            "energy_kJ": 0,
            "protein": 50,
            "carbohydrate": 275,
            "fibre": 28,
            "sugars": 0,
            "addedsugars": 50,
            "fat": 78,
            "saturated_fat": 20,
            "trans_fat": 0,
            "cholesterol": 300,
            "vitaminB6": 1.7,
            "vitaminD": 20,
            "calcium": 1300,
            "iron": 18,
            "phosphorus": 1250,
            "potassium": 4700,
            "sodium": 2300,
            "caffeine": 400,
        }

        productItemLoader = ItemLoader(item=McDonaldsItem(), response=response)
        jsonResponse = json.loads(response.body)
        itemId = str(jsonResponse["item"]["item_id"])
        productItemLoader.add_value("itemId", itemId)
        productItemLoader.add_value("itemName", jsonResponse["item"]["item_name"])
        # for cat in jsonResponse['item']['categories']['category']:
        #     print(cat)
        if jsonResponse["item"]["categories"]:
            categories = (
                {jsonResponse["item"]["categories"]["category"]["name"]}
                if "name" in jsonResponse["item"]["categories"]["category"]
                else {
                    cat["name"]
                    for cat in jsonResponse["item"]["categories"]["category"]
                }
            )
        else:
            categories = set()
        productItemLoader.add_value("categories", ", ".join(categories))
        if "component" in jsonResponse["item"]["components"]:
            allergens = {
                a.rstrip(".")
                for comp in jsonResponse["item"]["components"]["component"]
                if "product_allergen" in comp and comp["product_allergen"]
                for a in comp["product_allergen"].split(", ")
            }
        else:
            allergens = set()
        productItemLoader.add_value("allergens", ", ".join(allergens))
        productItemLoader.add_value(
            "menuItemNo", str(jsonResponse["item"]["menu_item_no"])
        )
        productItemLoader.add_value(
            "itemIngredientStatement", jsonResponse["item"]["item_ingredient_statement"]
        ) if jsonResponse["item"]["item_ingredient_statement"] else ""
        if "nutrient" in jsonResponse["item"]["nutrient_facts"]:
            for nutrient in jsonResponse["item"]["nutrient_facts"]["nutrient"]:
                nutrientName = nutrient["nutrient_name_id"]
                value = float(nutrient["value"])
                if dailyValue[nutrientName]:
                    productItemLoader.add_value(
                        f"{nutrientName}_DV",
                        str(value / dailyValue[nutrientName]),
                    )
                units = nutrient["uom_description"]
                productItemLoader.add_value(nutrientName, str(value))
                productItemLoader.add_value(f"{nutrientName}_units", units)
        self.visitedItemIds.add(itemId)
        yield productItemLoader.load_item()

        if jsonResponse["item"]["relation_types"]:
            for relatedType in jsonResponse["item"]["relation_types"]["relation_type"]:
                for item in relatedType["related_items"]["related_item"]:
                    if item["id"] != itemId and item["id"] not in self.visitedItemIds:
                        yield Request(
                            f"https://www.mcdonalds.com/wws/json/getItemDetails.htm?country=US&language=en&showLiveData=true&item={item['id']}",  # noqa: E501
                            method="GET",
                            callback=self.parse_details,
                        )
