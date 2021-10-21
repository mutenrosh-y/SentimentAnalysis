from p1 import *
import plotly.express as px
fig = plt.figure()
df_location_coordinates = pd.read_csv('LocationCoordinates.csv')
fig = px.scatter_geo(df_location_coordinates,lat='Latitude',lon='Londitude', locations='Locations', locationmode='country names', color=(['Neutral','Red','Positive'] * 20))
fig.update_layout(title = 'Product Locations WorldWide', title_x=0.5)
#plot by actual score values
fig.show()