# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter
from scrapy import signals
from scrapy.exporters import CsvItemExporter
from pydispatch import dispatcher

# class McdonaldsPipeline:
#     def process_item(self, item, spider):
#         return item

class MultiCSVItemPipeline(object):
    fileNamesCsv = ['McDonaldsItem']

    def __init__(self):
        self.files = {}
        self.exporters = {}
        dispatcher.connect(self.spider_opened, signal=signals.spider_opened)
        dispatcher.connect(self.spider_closed, signal=signals.spider_closed)


    def spider_opened(self, spider):
        self.files = dict([ (name, open(name+'.csv','ab')) for name in self.fileNamesCsv])
        for name in self.fileNamesCsv:
            self.exporters[name] = CsvItemExporter(self.files[name])
            if name == 'McDonaldsItem':                    
                self.exporters[name].fields_to_export = ['itemId', 'itemName', 'categories', 'allergens', 'menuItemNo', 
                    'calories', 'calories_DV', 'calories_units', 'calories_from_fat', 'calories_from_fat_DV', 
                    'calories_from_fat_units', 'energy_kJ', 'energy_kJ_DV', 'energy_kJ_units', 'protein', 'protein_DV', 
                    'protein_units', 'carbohydrate', 'carbohydrate_DV', 'carbohydrate_units', 'fibre', 'fibre_DV', 
                    'fibre_units', 'sugars', 'sugars_DV', 'sugars_units', 'addedsugars', 'addedsugars_DV', 
                    'addedsugars_units', 'fat', 'fat_DV', 'fat_units', 'saturated_fat', 'saturated_fat_DV', 
                    'saturated_fat_units', 'trans_fat', 'trans_fat_DV', 'trans_fat_units', 'cholesterol', 'cholesterol_DV', 
                    'cholesterol_units', 'vitaminB6', 'vitaminB6_DV', 'vitaminB6_units', 'vitaminD', 'vitaminD_DV', 
                    'vitaminD_units', 'calcium', 'calcium_DV', 'calcium_units', 'iron', 'iron_DV', 'iron_units', 
                    'phosphorus', 'phosphorus_DV', 'phosphorus_units', 'potassium', 'potassium_DV', 'potassium_units', 
                    'sodium', 'sodium_DV', 'sodium_units', 'caffeine', 'caffeine_DV', 'caffeine_units', 'itemIngredientStatement']
            self.exporters[name].start_exporting()

    def spider_closed(self, spider):
        [e.finish_exporting() for e in self.exporters.values()]
        [f.close() for f in self.files.values()]

    def item_type(self, item):
        return str(type(item)).split('.')[2].rstrip("'>")

    def process_item(self, item, spider):
        typesItem = self.item_type(item)
        if typesItem in set(self.fileNamesCsv):
            self.exporters[typesItem].export_item(item)
        return item