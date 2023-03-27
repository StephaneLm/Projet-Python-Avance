import unittest
import pymongo
from scraper_produits import scrape


class TestScraper(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        # Connexion à la base de données MongoDB
        cls.client = pymongo.MongoClient('mongodb://localhost:27017/')
        cls.db = cls.client['test_db']
        cls.collection = cls.db['test_collection']
        
        # Suppression des éventuels documents existants dans la collection
        cls.collection.delete_many({})
        
        # Scraper les produits et les ajouter à la collection
        scrape(cls.collection)
        
    @classmethod
    def tearDownClass(cls):
        # Fermer la connexion à la base de données MongoDB
        cls.client.close()
        
    def test_collection_not_empty(self):
        # Vérifier que la collection contient des documents
        count = self.collection.count_documents({})
        self.assertGreater(count, 0)
        
    def test_product_fields_exist(self):
        # Vérifier que les documents de la collection contiennent les champs 'name' et 'price'
        for product in self.collection.find({}):
            self.assertIn('name', product)
            self.assertIn('price', product)