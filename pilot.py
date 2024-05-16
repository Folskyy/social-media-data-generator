import geopandas as gpd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import argparse

# input argument
argv = argparse.ArgumentParser()
argv.add_argument('points_number', type=int, help="Number of data points to plot.")
args = argv.parse_args()

# url = 'https://geodata.ucdavis.edu/gadm/gadm4.1/shp/gadm41_BRA_shp.zip'
# gdf = gpd.read_file(url)
gdf = gpd.read_file('files/BRA_shp.zip')

# dataframe to save latitude and longitude data
data = pd.DataFrame(columns=['latitude', 'longitude'])

min_lat, max_lat = -33.75, 5.27
min_lon, max_lon = -73.99, -34.79

for i in range(args.points_number):
    # 2 random numbers to represent longitude and latitude
    latitude = np.random.uniform(min=min_lat, max=max_lat)
    longitude = np.random.uniform(min=min_lon, max=max_lon)
    
    # # data normalization (lat=5:-33; long=180:-180)
    # latitude = latitude * 40 - 35
    # longitude = longitude * 40 - 70

    # inserção de um novo par de dados no dataframe
    data.loc[i, ['latitude', 'longitude']] = (latitude, longitude)

gdf2 = gpd.GeoDataFrame(data, geometry=gpd.points_from_xy(data['longitude'], data['latitude'], crs="EPSG:4326"))

ax = gdf.plot(color='white', edgecolor='black')
# visualização
gdf2.plot(ax=ax, color='red')
plt.show()

gdf.head()
