import geopandas as gpd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import argparse

# Input argument
argv = argparse.ArgumentParser()
argv.add_argument('points_number', type=int, help="Number of data points to plot.")
argv.add_argument('shapefile', type=int, help="directory or link to a ShapeFile")
args = argv.parse_args()

br_shapefile = gpd.read_file(args.shapefile)
br_shapefile = gpd.read_file('files/BRA_shp.zip') # receber por parâmetro

# Dataframe to save latitude and longitude data
data = pd.DataFrame(columns=['latitude', 'longitude'])

# Brazil's geographic limitations
min_lat, max_lat = -33.75, 5.27
min_lon, max_lon = -73.99, -34.79

for i in range(args.points_number):
    # 2 random numbers to represent longitude and latitude
    latitude = np.random.uniform(min_lat, max_lat)
    longitude = np.random.uniform(min_lon, max_lon)

    # Data save on the dataframe
    data.loc[i, ['latitude', 'longitude']] = (latitude, longitude)

# Transform the dataframe saved into shapely points objects
geometry = gpd.points_from_xy(data['longitude'], data['latitude'], crs="EPSG:4326")
gdf = gpd.GeoDataFrame(data, geometry=geometry)

# Graph colors setting up and Brazil shapefile plot
ax = br_shapefile.plot(color='white', edgecolor='black')
# Points plot on top of the shapefile
gdf.plot(ax=ax, color='red')
plt.show()

# Iteractive map
m = br_shapefile.explore()
gdf.explore(m=m, color='red')

# Save all the explore() layers ploted before
m.save('map.html')

import webbrowser
# open the saved html file on the browser
webbrowser.open('map.html')
