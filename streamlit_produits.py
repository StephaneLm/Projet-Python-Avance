import pymongo
import streamlit as st
import plotly.express as px


client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['pc']
collection = db['ordinateur_portable']


st.sidebar.markdown(
"""
<style>
.sidebar .sidebar-content {
    background-color: #FF0000;
}
</style>
""",
unsafe_allow_html=True
)


data = []
for product in collection.find():
    name = product['name']
    price = product['price']
    data.append({'Nom': name, 'Prix': price})
    
df = px.data.tips()
df = px.histogram(data, x='Prix', nbins=20, title='Répartition des prix',color_discrete_sequence=['red'])
st.plotly_chart(df)


st.sidebar.header('Filtrage des produits')
filtre_nom = st.sidebar.text_input('Nom')
filtre_prix = st.sidebar.slider('Prix', 0, 100, (0, 100))


resultats_filtrage = []
for product in collection.find():
    name = product['name']
    price = product['price']
    if filtre_nom.lower() in name.lower() and filtre_prix[0] <= float(str(price).replace('€', '').replace(',', '.')) <= filtre_prix[1]:
        resultats_filtrage.append({'Nom': name, 'Prix': price})


if resultats_filtrage:
    st.write('Résultats du filtrage')
    st.table(resultats_filtrage)
else:
    st.write('Aucun produit n\'a été trouvé.')