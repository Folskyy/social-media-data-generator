from os import makedirs
import sys
import pandas as pd
import numpy as np
from shapely import Point
from datetime import datetime, timedelta

def insert_points_by_time(shapefile, point_num, start_time, end_time, temporal_comp):
    """
    Uses insert_points function to insert random points using a time componet who determines
    a time interval between the points.
    """
    actual_time = start_time
    delta = timedelta(minutes=temporal_comp)
    epochs = int(((end_time - start_time).total_seconds() / 60) // temporal_comp)
    actual_epoch = 0
    data = pd.DataFrame(columns=['latitude','longitude','time'])
    
    while actual_time < end_time:
        latitude, longitude, times = insert_points(shapefile,
                                                   point_num,
                                                   actual_time,
                                                   end_time)
        
        actual_epoch += 1
        sys.stdout.write(f'\n{actual_epoch}/{epochs} epochs...\n')

        actual_time += delta
        for i, j, k in zip(latitude, longitude, times):
            data.loc[len(data)] = [i, j, k]
    return data

def insert_points(shapefile, point_num, start_time, end_time):
    """
    Locates random points that are inside the shapefile and save their coordinates with a random
    time based on the interval of the times given.
    """
    latitude_points, longitude_points, times = [], [], []
    total_bounds = shapefile.total_bounds
    
    while len(latitude_points) < point_num:
        longitude = np.random.uniform(total_bounds[0], total_bounds[2])
        latitude  = np.random.uniform(total_bounds[1], total_bounds[3])
        random_point = Point(longitude, latitude)
        
        if shapefile.contains(random_point).any():
            latitude_points.append(latitude)
            longitude_points.append(longitude)
            
            time = np.random.uniform(start_time.timestamp(), end_time.timestamp())
            time = str(datetime.fromtimestamp(time))
            times.append(time)
            
            sys.stdout.write(f'\r{len(latitude_points)}/{point_num} points added.')
    
    return latitude_points, longitude_points, times

def out_dir(output_path):
        makedirs(output_path, exist_ok=True)