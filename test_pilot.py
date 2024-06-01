#%%
import geopandas as gpd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
#%%
# dados recebidos como parametro do programa
point_num = 10
temporal_comp = 10 # minutes
start_time = datetime.datetime(2024, 5, 28, 15, 43, 55)
end_time = datetime.datetime(2024, 5, 28, 18, 23, 50)

# Brazil shapefile download
br_shapefile = gpd.read_file('../files/BRA_shp.zip')

# Dataframe to save latitude and longitude data
data = pd.DataFrame(columns=['latitude', 'longitude'])

# Brazil's geographic limitations
min_lat, max_lat = -33.75, 5.27
min_lon, max_lon = -73.99, -34.79

#%%
actual_time = start_time
max_time, j = start_time, 0

while max_time < end_time:
    max_time = max_time + datetime.timedelta(minutes=temporal_comp)
    if max_time > end_time:
            max_time = end_time
    for i in range(point_num):
        # 2 random numbers to represent longitude and latitude
        latitude = np.random.uniform(min_lat, max_lat)
        longitude = np.random.uniform(min_lon, max_lon)

        time = float(np.random.uniform(actual_time.timestamp(), max_time.timestamp()))
        time = str(datetime.datetime.fromtimestamp(time))

        # Data save on the dataframe
        data.loc[j * i + i, ['latitude', 'longitude', 'time']] = (latitude, longitude, time)

    actual_time = actual_time + datetime.timedelta(minutes=temporal_comp)
    j += 1

#%%
# Transform the dataframe saved into shapely points objects
geometry = gpd.points_from_xy(data['longitude'], data['latitude'], crs="EPSG:4326")
gdf = gpd.GeoDataFrame(data, geometry=geometry)

#%%
# Graph colors setting up and Brazil shapefile plot
ax = br_shapefile.plot(color='white', edgecolor='black')
# Points plot on top of the shapefile
gdf.plot(ax=ax, color='red')
plt.show()

#%%
# **Only works on notebooks**
# Iteractive map
m = br_shapefile.explore()
# Points plot on top of the shapefile
gdf.explore(m=m, color='red')
# %%
