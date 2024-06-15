#%%
import geopandas as gpd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
from shapely import Point
#%%
# dados recebidos como parametro do programa
point_num = 10
temporal_comp = 10 # minutes
start_time = datetime.datetime(2024, 5, 28, 15, 43, 55)
end_time = datetime.datetime(2024, 5, 28, 18, 23, 50)

# Brazil shapefile download
br_shapefile = gpd.read_file('../files/BRA_shp.zip')

# Brazil's geographic limitations
min_lat, max_lat = -33.75, 5.27
min_lon, max_lon = -73.99, -34.79

#%%
def insert_points(shapefile, point_num, actual_time, max_time):
    latitude_points = []
    longitude_points = []
    times = []
    total_bounds = shapefile.total_bounds

    while len(latitude_points) < point_num:
        # 2 random numbers to represent longitude and latitude    
        longitude = np.random.uniform(total_bounds[0], total_bounds[2])
        latitude = np.random.uniform(total_bounds[1], total_bounds[3])
        
        random_point = Point(longitude, latitude)
        if shapefile.contains(random_point).any():
            print(f'point[{len(latitude_points)}] founded')
            latitude_points.append(latitude)
            longitude_points.append(longitude)
            time = np.random.uniform(actual_time.timestamp(), max_time.timestamp())
            time = str(datetime.datetime.fromtimestamp(time))
            times.append(time)
        
    return latitude_points, longitude_points, times
#%% timestamp
actual_time = start_time
max_time = start_time  
lat_points, lon_points, times = [], [], []
while max_time < end_time:
    max_time += datetime.timedelta(minutes=temporal_comp)
    if max_time > end_time:
            max_time = end_time
    lat, lon, time = insert_points(br_shapefile, point_num, actual_time, max_time)
    [lat_points.append(item) for item in lat]
    [lon_points.append(item) for item in lon]
    [times.append(item) for item in time]
    actual_time = actual_time + datetime.timedelta(minutes=temporal_comp)

#%% # no timestamp
lat_points, lon_points, times = insert_points(br_shapefile, point_num, start_time, end_time)
#%%
# Transform the dataframe saved into shapely points objects
geometry = gpd.points_from_xy(lon_points, lat_points, crs="EPSG:4326")
gdf = gpd.GeoDataFrame(pd.DataFrame({'longitude': lon_points, 'latitude': lat_points, 'time': times}), geometry=geometry)

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
