# McDonaldsCrawler
McDonaldsCrawler is an application designed to scrape all McDonalds menu items for the followng nutrition information:

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

All the nutrition data is summarized into a [Google Data Studio dashboard](https://datastudio.google.com/reporting/fa582f39-db39-4ab0-bffe-2acb5ef6f2f3) or [Tableau Public dashboard](https://public.tableau.com/app/profile/pat3330/viz/McDonaldsNutrition_16413257497100/McDonaldsNutrition?publish=yes).
## Google Data Studio Dashboard - Screenshots
![McDonaldsNutrition](https://user-images.githubusercontent.com/60832092/144688730-263be295-2c66-4d48-8a80-ba1e4daf2064.PNG)
![MostCalories](https://user-images.githubusercontent.com/60832092/144688759-decc3171-675e-4c99-928e-744002774848.PNG)

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