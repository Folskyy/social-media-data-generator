import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import argparse
from utilities import insert_points
from datetime import datetime

argv = argparse.ArgumentParser()
argv.add_argument('points_number', type=int, help="Number of data points to plot.")
argv.add_argument('temporal_component', type=int, help="Time update interval")
argv.add_argument('start_timestamp', type=int, help="Time update interval")
argv.add_argument('end_timestamp', type=int, help="Time update interval")
argv.add_argument('shapefile', type=str, help="directory or link to a ShapeFile")

args = argv.parse_args()

# variables definition
points_num = args.points_number
temporal_comp = args.temporal_component
shapefile = gpd.read_file(args.shapefile)
start_time = datetime.fromtimestamp(args.start_timestamp)
end_time = datetime.fromtimestamp(args.end_timestamp)

latitude, longitude, times = insert_points(shapefile,
                                           points_num,
                                           start_time,
                                           end_time)

data = pd.DataFrame({'latitude': latitude,
                     'longitude': longitude,
                     'times': times
                     })

# Transform the dataframe saved into shapely points objects
geometry = gpd.points_from_xy(data['longitude'],
                              data['latitude'],
                              crs="EPSG:4326")
gdf = gpd.GeoDataFrame(data, geometry=geometry)

# Graph colors setting up and Brazil shapefile plot
ax = shapefile.plot(color='white', edgecolor='black')
# Points plot on top of the shapefile
gdf.plot(ax=ax, color='red')
plt.show()

# Iteractive map
m = shapefile.explore()
gdf.explore(m=m, color='red')

# Save all the explore() layers ploted before
m.save('map.html')

import webbrowser
# open the saved html file on the browser
webbrowser.open('map.html')
