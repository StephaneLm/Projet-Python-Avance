user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36'
headers = {'User-Agent': user_agent}
from bs4 import BeautifulSoup
import requests
import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['pc']
collection = db['ordinateur_portable']


url = 'https://fr.aliexpress.com/w/wholesale-%C3%A9cran.html?catId=0&initiative_id=SB_20230326140436&SearchText=%C3%A9cran&spm=a2g0o.productlist.1000002.0'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser') #Objet BeautifulSoup

produits = soup.find_all('div', class_='manhattan--content--1KpBbUi') #Recherche éléments HTML

data = []
for produit in produits:
    name = produit.find('h1', class_='manhattan--titleText--WccSjUS').text.strip()
    price = produit.find('div', class_='manhattan--price-sale--1CCSZfK').text.strip()
    data = {'name': name, 'price': price}
    collection.insert_one(data)
    
#On reprends ce qui a été fait au dessus pour faire la fonction de test unitaire
def scrape(url):
    # création d'une session pour gérer les cookies
    session = requests.Session()

    # récupération du contenu HTML de la page web
    response = session.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    # recherche des éléments HTML appropriés
    products = soup.find_all('div', class_='manhattan--content--1KpBbUi')

    # stockage des données dans un tableau
    data = []
    for product in products:
        name = product.find('h1', class_='manhattan--titleText--WccSjUS').text.strip()
        price = product.find('div', class_='manhattan--price-sale--1CCSZfK').text.strip()
        data.append({'name': name, 'price': price})

    return data