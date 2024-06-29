import geopandas as gpd
import numpy as np
from shapely import Point
import datetime

def insert_points(shapefile, point_num, actual_time, max_time):
    latitude_points, longitude_points, times = [], [], []
    total_bounds = shapefile.total_bounds

    while len(latitude_points) < point_num:
        # 2 random numbers to represent longitude and latitude    
        longitude = np.random.uniform(total_bounds[0], total_bounds[2])
        latitude  = np.random.uniform(total_bounds[1], total_bounds[3])
        random_point = Point(longitude, latitude)
        
        if shapefile.contains(random_point).any():
            print(f'point[{len(latitude_points)}] founded')
            latitude_points.append(latitude)
            longitude_points.append(longitude)
            time = np.random.uniform(actual_time.timestamp(), max_time.timestamp())
            time = str(datetime.datetime.fromtimestamp(time))
            times.append(time)
        
    return latitude_points, longitude_points, times