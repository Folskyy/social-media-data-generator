import geopandas as gpd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import argparse

# input argument
entrada = argparse.ArgumentParser()
entrada.add_argument('points_number', type=int, help="Number of data points to plot.")
args = entrada.parse_args()

# url = 'https://geodata.ucdavis.edu/gadm/gadm4.1/shp/gadm41_BRA_shp.zip'
# gdf = gpd.read_file(url)
gdf = gpd.read_file('files/BRA_shp.zip')

# dataframe to save latitude and longitude data
data = pd.DataFrame(columns=['latitude', 'longitude'])

for i in range(args.points_number):
    # geração de 2 números aleatórios para a longitude e latitude
    latitude, longitude = np.random.rand(2)
    
    # normalização dos números aleatórios gerados (lat=90:-90; long=180:-180)
    latitude = latitude * 40 - 35
    longitude = longitude * 40 - 70

    # inserção de um novo par de dados no dataframe
    data.loc[i, ['latitude', 'longitude']] = (latitude, longitude)

# conversão de um dataframe para um geodataframe
# PARAMETROS:
# data -> conjunto de dados para formar uma tabela
# geometry -> formação de dados geométricos.
# foi utilizado o gpd.points_from_xy para transformar lat e long em uma
# lista de Pontos (shapely.Points) e interpretá-los como um objeto geometry
# crs -> sistema de referencia. Ele define o sistema de coordenadas utilizado
# para representar a localização espacial de dados geográficos.
# , crs="EPSG:4326"
# coordenadas = list(zip(data['latitude'], data['longitude']))

gdf2 = gpd.GeoDataFrame(data, geometry=gpd.points_from_xy(data['longitude'], data['latitude'], crs="EPSG:4326"))

ax = gdf.plot(color='white', edgecolor='black')
# visualização
gdf2.plot(ax=ax, color='red')
plt.show()

gdf.head()
