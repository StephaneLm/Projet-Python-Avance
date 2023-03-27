import unittest
import pymongo
from scraper_produits import scrape


class TestScraper(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.client = pymongo.MongoClient('mongodb://localhost:27017/')
        cls.db = cls.client['test_db']
        cls.collection = cls.db['test_collection']
        
        #Suprr si existe
        cls.collection.delete_many({})
        
        # Fonction dans scraper_produits qui scrape les produits et les ajoute à la collection
        scrape(cls.collection)
        
    @classmethod
    def closeCo(cls):
        cls.client.close()
        
    def test_collection_vide(self):
        count = self.collection.count_documents({})
        self.assertGreater(count, 0)
        
    def test_product_existe(self):
        for product in self.collection.find({}):
            self.assertIn('name', product)
            self.assertIn('price', product)