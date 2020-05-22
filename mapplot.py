
import geopandas
import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('/home/kristian/Desktop/pumps/pumps.csv', index_col=0)
df = df[df['longitude'] > 0.0]

gdf = geopandas.GeoDataFrame(df, geometry=geopandas.points_from_xy(df['longitude'], df['latitude']))

world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))

#ax = world[world.continent == 'Africa'].plot(color='white', edgecolor='black')
# ax = world[world.name == 'Tanzania'].plot(color='white', edgecolor='black')
ax = world[world.name.isin(['Tanzania', 'Kenya', 'Uganda', 'Mozambique', 'Zambia'])].plot(color='white', edgecolor='black')

gdf.plot(ax=ax, color='red', markersize=0.2)

plt.show()
