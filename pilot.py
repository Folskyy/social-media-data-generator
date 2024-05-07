#%%
import geopandas as gpd
import pandas as pd
import numpy as np
# from shapely import Point

#%%
# leitura do número de pontos a serem inseridos
entrada = int(input("Insira o número de pontos a ser plotado:\n> "))

# cria um dataframe para armazenar os dados da latitude e longitude
data = pd.DataFrame(columns=['latitude', 'longitude'])

#%%
for i in range(entrada):
    # geração de 2 números aleatórios para a longitude e latitude
    latitude, longitude = np.random.rand(2)
    
    # normalização dos números aleatórios gerados (lat=90:-90; long=180:-180)
    latitude = 180 * (latitude - 0.5)
    longitude = 360 * (longitude - 0.5)

    # inserção de um novo par de dados no dataframe
    data.loc[i, ['latitude', 'longitude']] = (latitude, longitude)

#%%
# conversão de um dataframe para um geodataframe
# PARAMETROS:
# data -> conjunto de dados para formar uma tabela
# geometry -> formação de dados geométricos.
# foi utilizado o gpd.points_from_xy para transformar lat e long em uma
# lista de Pontos (shapely.Points) e interpretá-los como um objeto geometry
# crs -> sistema de referencia. Ele define o sistema de coordenadas utilizado
# para representar a localização espacial de dados geográficos.
gdf = gpd.GeoDataFrame(data, geometry=gpd.points_from_xy(data['latitude'], data['longitude'], crs="EPSG:4326"))
#%%
gdf.plot()
gdf.head()
# %%
