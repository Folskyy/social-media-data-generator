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
# br_shapefile = gpd.read_file(url)
br_shapefile = gpd.read_file('files/BRA_shp.zip')

# dataframe to save latitude and longitude data
data = pd.DataFrame(columns=['latitude', 'longitude'])

# Brazil's geographic limitations
min_lat, max_lat = -33.75, 5.27
min_lon, max_lon = -73.99, -34.79

for i in range(args.points_number):
    # 2 random numbers to represent longitude and latitude
    latitude = np.random.uniform(min_lat, max_lat)
    longitude = np.random.uniform(min_lon, max_lon)

    # data save on the dataframe
    data.loc[i, ['latitude', 'longitude']] = (latitude, longitude)

# transform the dataframe saved to shapely points objects
geometry = gpd.points_from_xy(data['longitude'], data['latitude'], crs="EPSG:4326")
gdf = gpd.GeoDataFrame(data, geometry=geometry)

# graph colors setting up and brazil shapefile plot
ax = br_shapefile.plot(color='white', edgecolor='black')
# points plot upside the shapefile
gdf.plot(ax=ax, color='red')
plt.show()
