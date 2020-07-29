import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import numpy as np

# assign the extent values
xmin, xmax, ymin, ymax = -179, 179, -89, 89

# create a random numpy list of longitudes within xmin <> xmax range
xs = np.random.uniform(low=xmin,high=xmax,size=(1000,))
# create a random numpy list of latitudes within ymin <> ymax range
ys = np.random.uniform(low=ymin,high=ymax,size=(1000,))
# numpy column_stack method creates multidimensional array from single-dimensional arrays
arr = np.column_stack((xs, ys))
# create a dataframe with the index list and the two numpy arrays
random_df = pd.DataFrame(arr,columns=['lon','lat'])
############################
# store the dataframe as csv
############################
random_df.to_csv('./data/xys.csv', index=False)
#######################################
# create geodf and store it as geojson
#######################################
# create a geodataframe using the random_df
random_gdp = gpd.GeoDataFrame(random_df, geometry=gpd.points_from_xy(random_df.Longitude, random_df.Latitude),crs='EPSG:4326')
# save the geodataframe to geojson file
random_gdp.to_file('./data/xys.geojson',driver='GeoJSON')
