from geopy.geocoders import Nominatim
from players_dict import player_uni_dict
import plotly.plotly as py
import pandas as pd
import csv

def get_location(uni):
    a = "University of"
    b = "University"
    geolocator = Nominatim(user_agent="my_map")
    location = geolocator.geocode(uni)
    location2 = geolocator.geocode(a + uni)
    location3 = geolocator.geocode(uni + b)

    if location is not None:
        return(location)
    elif location2 is not None:
        return(location2)
    else:
        return(location3)

lat_long_dict = {}

for player, university in player_uni_dict.items():
    try:
        location = get_location(university)
        lat_long = {}
        lat_long["latitude"] = location.latitude
        lat_long["longitude"] = location.longitude
        lat_long["location"] = location
        lat_long_dict[player] = lat_long
    except Exception as e:
        continue

with open('player_file.csv', mode='w') as player_file:
    player_writer = csv.writer(player_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    player_writer.writerow(['Player', 'Location', 'Latitude', 'Longitude'])
    for player, latlong in lat_long_dict.items():
        player_writer.writerow([player, latlong['location'], latlong['latitude'], latlong['longitude']])

player_lat_long = pd.read_csv('player_file.csv')

data = [dict(
   type = 'scattergeo',
    locationmode = 'USA-states',
    lon = player_lat_long['Longitude'],
    lat = player_lat_long['Latitude'],
    text = player_lat_long['Player'] + ' ' + player_lat_long['Location'],
    mode = 'markers'
    )]

layout = dict(
    title = '49ers',
    geo = dict(
      scope='usa',
      projection=dict( type='albers usa' ),
      showland = True,
      landcolor = "rgb(250, 250, 250)",
      subunitcolor = "rgb(217, 217, 217)",
      countrycolor = "rgb(217, 217, 217)",
      countrywidth = 0.5,
      subunitwidth = 0.5
      )
)

fig = dict(data=data, layout=layout)
py.plot(fig, validate=False, filename='player_file.csv')
