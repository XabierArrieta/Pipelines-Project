# Project: Data Pipeline - Madrid Airbnb

## Introducción:

Airbnb es una compañía creada en 2008 por Brian Chesky, que ofrece una plataforma digital dedicada a la oferta de alojamientos a particulares y turísticos (alquiler vacacional) mediante la cual los anfitriones pueden publicitar y contratar el arriendo de sus propiedades con sus huéspedes; anfitriones y huéspedes pueden valorarse mutuamente, como referencia para futuros usuarios. El nombre es un acrónimo de airbed and breakfast.
​
Airbnb tiene una oferta de unas 2 000 000 propiedades en 192 países y 33 000 ciudades. En España aterrizó en el año 2008.

En 2019, la ciudad de Madrid registró en la llegada de 10,4 millones de visitantes, de los cuales el 55% fueron internacionales y el 45% nacionales. Se generaron 22,6 millones de pernoctaciones. 

Los principales mercados emisores de turismo internacional fueron Estados Unidos, Italia, Francia, Reino Unido y Alemania y los que más crecieron, Estados Unidos, China, Italia, Brasil y México. Se alcanzó un gasto total de 10.451 millones y un gasto medio diario de 270 euros en la Comunidad de Madrid. 


## Objetivo:

Este es un proyecto que lo he realizado durante el Bootcamp de Data Anatlytics en [Ironhack](https://www.ironhack.com/es/data-analytics) Maddrid.

El objetivo es;

-   Escoger una base de datos de [Kaggle](www.kaggle.com).
-   Limpiar la base de datos.
-   Enriquecerla, a través de wev scraping o Api.
-   Visualizar los datos obtenidos con gráficos.

Las libreias usadas en este proyecto: Pandas, Sys, Requests, BeautifulSoup, Geocoder,Seaborn, matplotlib.pyplot.


## Proceso:

He escogido una base de datos de [Airbnb de Madrid Dataset](https://www.kaggle.com/rusiano/madrid-airbnb-data) con una usabilidad de 9,4 compuesto de 20837 filas y 16 columnas. En esta base de datos se muestran datos de los apartamentos que Airbnb tiene en la ciudad de Madrid en base a su ubicación, precio, número de comentarios entre otros.

Los pasos a seguir;

-   Analizar el dataset; ya está bastante limpio por lo que reviso las columnas, quito los valores nulos, duplicados y las columnas no necesarias para mi análisis. Además cambio los caracteres especiales, cómo los acentos. (cleaning.ipynb)
-   Web scraping; una vez que tengo el dataset limpio decido enriquecerlo con información relacionada con los monumentos de interés cercanos a los apartamentos. Además, con Geocoder, consigo añadir la longitud y latitud y calcular la distancia al monumento más cercano. (Web scraping.ipynb)
-   Visualización: Observando los precios, distritos, barrios y monumentos, realizo diferentes gráficos.(Visualización.ipynb)
-   Resultados: Por último destaco las conclusiones;

    - Los barrios donde más apartamentos se ofrecen son: Centro, Salamanca y Chamberí.
    - La mayoría de ellos están cerca de los principales puntos de interés de Madrid: Malasaña, Barrio de las Letras y el Estadio Santiago Bernabeu.
    
    - ¿Quieres saber cuanto cuesta el apartamento más caro? y, ¿el más barato?
    Te invito a que lo descubras tu mismo.
 
## Enlaces:

- [Kaggle](www.kaggle.com)
- [Airbnb de Madrid Dataset](https://www.kaggle.com/rusiano/madrid-airbnb-data)
- [Airbnb](https://www.airbnb.es/madrid-spain/stays) 
- [Sitios de interés en Madrid](https://www.tripadvisor.es/Attractions-g187514-Activities-c47-Madrid.html)
- [Madrid Destino](https://www.madrid-destino.com/)
