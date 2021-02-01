import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json
import statistics 
import src.cleaning_func as cf
import sys
sys.path.append("../")
import requests
from bs4 import BeautifulSoup




def cleaning_mad(mad):
    
    # Eliminar columnas no relevantes para el análisis.
    
    mad = mad.drop(['minimum_nights', 'last_review', 'reviews_per_month', 'calculated_host_listings_count', 'availability_365'], axis = 1 )
    # Contar valores nulos.

    mad.isnull().sum().sort_values(ascending=False)
    
    # Elimininar valores nulos.
    
    mad.dropna()
    
    # Eliminar valore duplicados.
    
    mad.drop_duplicates()
    
    # Mostrar distritos correctamente.

def dist(nombre):
    if nombre == 'ChamartÃ\xadn':
        return 'Chamartin'
    elif nombre== 'TetuÃ¡n':
        return 'Tetuan'
    elif nombre == 'ChamberÃ\xad':
        return 'Chamberí'
    elif nombre == 'VicÃ¡lvaro':
        return 'nombre'
        
    # Reemplazar caracteres especiales en los barrios.
    
def carac(nombre):
    if 'Ã¡' in nombre:
        return nombre.replace('Ã¡','á')
    elif 'Ã©' in nombre:
        return nombre.replace('Ã©','é')
    elif 'Ã\xad' in nombre: 
        return nombre.replace('Ã\xad','í')
    elif 'Ã³'in nombre:
        return nombre.replace('Ã³','ó')
    elif 'Ãº'in nombre:
        return nombre.replace('Ãº', 'ú')
    elif 'Ã¼' in nombre:
        return nombre.replace('Ã¼','ü')
    else:
        return nombre
    
    
 

def scraping(mad_ready):
    #Abrir la database
    mad.to_csv("mad_for_vis.csv", encoding='utf-8-sig') 
    #poner url
    url_mad = "https://www.tripadvisor.es/Attractions-g187514-Activities-c47-Madrid.html"
    response = requests.get(url_mad)
    response
    soup = BeautifulSoup(response.content)
    #saca los titulos
    mad_att = soup.select("h2")
    #quita espacios
    mad_att[0].text.strip()
    #aplica función
    att = [(i.text.strip()) for i in mad_att]
    #crea nuevo dataframe
    att = pd.DataFrame(att, columns=['attractions'])
    # uso geocoder
    geocoder.osm("Palacio Real de Madrid, Madrid").json
    
def lat_long():   
    lat = []
    long = []
    for m in monuments["name"]:
        data = geocoder.osm(f"{m}, Madrid").json
        if data:
            lat.append(data.get('lat', None))
            long.append(data.get('lng', None))
        else:
            lat.append(None)
            long.append(None)
    
def dist_mon():
for  i, fila in mad.iterrows():
    lista = [fila["latitude"],fila["longitude"]]#muestra las filas con la latitud y longitud
    print(monuments.loc[monuments.apply(lambda row: haversine(lista,[row["latitude"],row["longitude"]]), axis=1).argmin()]["name"])#muestra la serie con la distancia en km con el loc accedemos al monumento más cercano y si ponemos el nombre nos dice el ordén del monumenrto más cercano.    

def cercano():
closest = []
for  i, fila in mad.iterrows():
    lista = [fila["latitude"],fila["longitude"]]#muestra las filas con la latitud y longitud
    closest.append(monuments.loc[monuments.apply(lambda row:haversine(lista,[row["latitude"],row["longitude"]]), axis=1).argmin()]["name"])   