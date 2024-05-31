#%%
import geopandas as gpd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
#%%
point_num = 10
temporal_comp = 10 # minutes
start_time = datetime.datetime(2024, 5, 28, 15, 43, 55)
end_time = start_time + datetime.timedelta(minutes = temporal_comp)

# Brazil shapefile download
br_shapefile = gpd.read_file('files/BRA_shp.zip')

# Dataframe to save latitude and longitude data
data = pd.DataFrame(columns=['latitude', 'longitude'])

# Brazil's geographic limitations
min_lat, max_lat = -33.75, 5.27
min_lon, max_lon = -73.99, -34.79

#%%
for i in range(point_num):
    # 2 random numbers to represent longitude and latitude
    latitude = np.random.uniform(min_lat, max_lat)
    longitude = np.random.uniform(min_lon, max_lon)
    actual_time = str(start_time + datetime.timedelta(minutes=i))

    # Data save on the dataframe
    data.loc[i, ['latitude', 'longitude', 'time']] = (latitude, longitude, actual_time)

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
