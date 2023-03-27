# Projet-Python-Avance
### Rendu du projet 

# Scraper Produits:
Ce code Python utilise la bibliothèque BeautifulSoup, la bibliothèque requests et la base de données MongoDB pour extraire les noms et les prix des ordinateurs portables à partir d'un site Web.

Pour exécuter le programme, il suffit de lancer le script avec la commande python ---> python scraper_produits.py. Le script extrait les données à partir du site web Aliexpress regroupant des articles divers et variées et les stocke dans la base de données MongoDB (on peux voir la base sur MongoDBCompass plus facilement).

Les données sont stockées dans la collection ordinateur_portable de la base de données pc.


# Streamlit Produits:
Ce code Python utilise la bibliothèque Streamlit et la base de données MongoDB pour créer une application Web permettant de filtrer des produits variées d'Aliexpress.

Pour exécuter le programme, utilisez la commande streamlit ---> streamlit run streamlit_pc_portable.py

Une fois l'application chargée, utiliser le panneau latéral pour filtrer les produits en fonction du nom et du prix. Les résultats filtrés s'affichent dans un tableau sous le panneau latéral.

Si aucun produit ne correspond aux critères de filtrage, un message "Aucun produit n'a été trouvé." s'affichera à la place du tableau de résultats.


# Tests unitaires

Pour le test unitaire on le lance avec la commande python suivante : python test_scraper.py

Avec les fonctions du fichier nous testons que le scraper fonctionne bien, si nous pouvons bien fermer la connexion à la base de donnée, si la collection est vide et si les produits existe bien.
