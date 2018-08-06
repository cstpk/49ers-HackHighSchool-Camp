from geopy.geocoders import Nominatim
from datetime import datetime
import plotly.plotly as py
import csv
# import pprint
#
# pp = pprint.PrettyPrinter(indent=4)

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

player_uni_dict = {
  'Wes Saxton': 'South Alabama',
  'JP Flynn': 'Montana State',
  'Will Sutton': 'Arizona State',
  'Cedric Thornton': 'Southern Arkansas',
  'Mike Person': 'Montana State',
  'Coleman Shelton': 'Washington',
  'Jeff Wilson': 'North Texas',
  'Corey Griffin': 'Georgia Tech',
  'Najee Toran': 'UCLA',
  'Alan Knott': 'South Carolina',
  'Jack Heneghan': 'Dartmouth',
  'Emmanuel Moseley': 'Tennessee',
  'Tarvarus McFadden': 'Florida State',
  'Niles Scott': 'Frostburg State',
  'Terrell Williams': 'Houston',
  'Ross Dwelley': 'San Diego',
  'Steven Dunbar Jr.': 'Houston',
  'Richie James Jr.': 'Middle Tennessee State',
  'Jullian Taylor': 'Temple',
  'Marcell Harris': 'Florida',
  'D.J. Reed Jr.': 'Kansas State',
  'Tarvarius Moore': 'Southern Miss',
  'Fred Warner': 'BYU',
  'Dante Pettis': 'Washington',
  'Mike McGlinchey': 'Notre Dame',
  'Korey Toomer': 'Idaho',
  'Jonathan Cooper': 'North Carolina',
  'Jeff Locke': 'UCLA',
  'Jeremiah Attaochu': 'Georgia Tech',
  'Weston Richburg': 'Colorado State',
  'Jerick McKinnon': 'Georgia Southern',
  'Richard Sherman': 'Stanford',
  'Malcolm Johnson': 'Mississippi State',
  'Elijah Lee': 'Kansas State',
  'Mark Nzeocha': 'Wyoming',
  'Bradley Pinion': 'Clemson',
  'Tyvis Powell': 'Ohio State',
  'Aldrick Robinson': 'Southern Methodist',
  'Joe Staley': 'Central Michigan',
  'Malcolm Smith': 'USC',
  'Andrew Lauderdale': 'New Hampshire',
  'Ahkello Witherspoon': 'Colorado',
  'Joe Williams': 'Utah',
  "K'Waun Williams": 'Pittsburgh',
  'Darrell Williams Jr.': 'Western Kentucky',
  'Cole Wick': 'Incarnate Word (Tex.)',
  'Dekoda Watson': 'Florida State',
  'Max McCaffrey': 'Duke',
  'Jimmie Ward': 'Northern Illinois',
  'Laken Tomlinson': 'Duke',
  'Solomon Thomas': 'Stanford',
  'Trent Taylor': 'Louisiana Tech',
  'Jeremy McNichols': 'Boise State',
  'Pita Taumoepenu': 'Utah',
  'Greg Mabin': 'Iowa',
  'Jaquiski Tartt': 'Samford',
  'Erik Magnuson': 'Michigan',
  'Cassius Marsh': 'UCLA',
  'Chanceller James': 'Boise State',
  'Kyle Nelson': 'New Mexico State',
  'Pace Murphy': 'Northwestern State-Louisiana',
  'Joshua Garnett': 'Stanford',
  'Earl Mitchell': 'Arizona',
  'Cole Hikutini': 'Louisville',
  'Eli Harold': 'Virginia',
  'Raheem Mostert': 'Purdue',
  'Robbie Gould': 'Penn State',
  'Nick Mullens': 'Southern Mississippi',
  'Marquise Goodwin': 'Texas',
  'Garry Gilliam': 'Penn State',
  'George Kittle': 'Iowa',
  'Reuben Foster': 'Alabama',
  'Antone Exum Jr.': 'Virginia Tech',
  'Sheldon Day': 'Notre Dame',
  'Brock Coyle': 'Montana',
  'Adrian Colbert': 'Miami (Fla.)',
  'Garrett Celek': 'Michigan State',
  'Aaron Burbridge': 'Michigan State',
  'DeForest Buckner': 'Oregon',
  'Kendrick Bourne': 'Eastern Washington',
  'Matt Breida': 'Georgia Southern',
  'Victor Bolden Jr.': 'Oregon State',
  'Ronald Blair III': 'Appalachian State',
  'C.J. Beathard': 'Iowa',
  'Arik Armstead': 'Oregon',
  'D.J. Jones': 'Mississippi',
  'Pierre Garon': 'Mount Union',
  'Jimmy Garoppolo': 'Eastern Illinois',
  'Kyle Juszczyk': 'Harvard'
 }

lat_long_dict = {}

for player, university in player_uni_dict.items():
    try:
        location = get_location(university)
        lat_long = {}
        lat_long["latitude"] = location.latitude
        lat_long["longitude"] = location.longitude
        lat_long_dict[player] = lat_long
    except Exception as e:
        continue

with open('player_file.csv', mode='w') as player_file:
    player_writer = csv.writer(player_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    player_writer.writerow(['Player', 'Latitude', 'Longitude'])
    for player, latlong in lat_long_dict.items():
        player_writer.writerow([player, latlong['latitude'], latlong['longitude']])

# pp.pprint(lat_long_dict)

# data = [dict(
#    type = 'scattergeo',
#     locationmode = 'USA-states',
#     lon = latlong['longitude'],
#     lat = latlong['latitude'],
#     text = [player],
#     mode = 'markers'
#     )]
#
# layout = dict(
#     title = '49ers'
# )
#
# geo = dict(
#       scope='usa',
#       projection=dict( type='albers usa' ),
#       showland = True,
#       landcolor = "rgb(250, 250, 250)",
#       subunitcolor = "rgb(217, 217, 217)",
#       countrycolor = "rgb(217, 217, 217)",
#       countrywidth = 0.5,
#       subunitwidth = 0.5
# )

# fig = dict(data=data, layout=layout)
# py.plot(fig, validate=False, filename='CampaignFinancestuff')
