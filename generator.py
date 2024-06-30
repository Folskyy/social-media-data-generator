import argparse
import pandas as pd
import geopandas as gpd
from datetime import datetime
import matplotlib.pyplot as plt
from utilities import insert_points_by_time

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

data = pd.DataFrame(insert_points_by_time(shapefile,
                                          points_num,
                                          start_time,
                                          end_time,
                                          temporal_comp))

geometry = gpd.points_from_xy(data['longitude'],
                              data['latitude'],
                              crs="EPSG:4326")
gdf = gpd.GeoDataFrame(data, geometry=geometry)

ax = shapefile.plot(color='white', edgecolor='black')
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
