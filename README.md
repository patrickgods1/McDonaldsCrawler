# McDonaldsCrawler
McDonaldsCrawler is an application designed to scrape all WeWork locations for the followng information:

* itemId
* itemName
* categories
* allergens
* menuItemNo
* calories
* calories_DV
* calories_units
* calories_from_fat
* calories_from_fat_DV
* calories_from_fat_units
* energy_kJ
* energy_kJ_DV
* energy_kJ_units
* protein
* protein_DV
* protein_units
* carbohydrate
* carbohydrate_DV
* carbohydrate_units
* fibre
* fibre_DV
* fibre_units
* sugars
* sugars_DV
* sugars_units
* addedsugars
* addedsugars_DV
* addedsugars_units
* fat
* fat_DV
* fat_units
* saturated_fat
* saturated_fat_DV
* saturated_fat_units
* trans_fat
* trans_fat_DV
* trans_fat_units
* cholesterol
* cholesterol_DV
* cholesterol_units
* vitaminB6
* vitaminB6_DV
* vitaminB6_units
* vitaminD
* vitaminD_DV
* vitaminD_units
* calcium
* calcium_DV
* calcium_units
* iron
* iron_DV
* iron_units
* phosphorus
* phosphorus_DV
* phosphorus_units
* potassium
* potassium_DV
* potassium_units
* sodium
* sodium_DV
* sodium_units
* caffeine
* caffeine_DV
* caffeine_units
* itemIngredientStatement

## Development
These instructions will get you a copy of the project up and running on your local machine for development.

### Built With
* [Python 3.6](https://docs.python.org/3/) - The scripting language used.
* [Scrapy](https://scrapy.org/) - Framework for crawling and extracting the data from webpages.

### Running the Script
Run the following command to installer all the required Python modules:
```
pip install -r requirements.txt
```

To run the application, call the following in the root directory of the project:
```
scrapy crawl scrapeMcDonalds
```

## Authors
* **Patrick Yu** - *Initial work* - [patrickgods1](https://github.com/patrickgods1)