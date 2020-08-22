
from urllib.request import urlopen
import pprint
import json
import pandas as pd
from apis import spotify

def get_file_path(file_name):
    import os
    import sys
    dir_path = os.path.dirname(sys.argv[0])
    return os.path.join(dir_path, file_name)

# --------------------------------------------------------------------------------
# ## 1. Go and get the Google Homepage
# --------------------------------------------------------------------------------

# 1. get it from the internet
response = urlopen('https://www.google.com')
file_data = response.read().decode('utf-8', 'ignore')

# 2. print it to the screen
print(file_data)

# 3. write it to a file
file_path = get_file_path('results/google_homepage.html')
f = open(file_path, 'w')
f.write(file_data)
f.close()
print('Web page written to results/google_homepage.html. Go take a look!')



# --------------------------------------------------------------------------------
# ## 2. Go and get a cat photo
# --------------------------------------------------------------------------------

# 1. get it from the internet
response = urlopen('https://kittenrescue.org/wp-content/uploads/2017/03/KittenRescue_KittenCareHandbook.jpg')
file_data = response.read()

# 2. print it to the screen
# print(file_data)

# 3. write it to a file
file_path = get_file_path('results/kitten.jpg')
f = open(file_path, 'wb')  #note the 'wb' flag (b is for binary)
f.write(file_data)
f.close()
print('Image written to results/kitten.jpg. Go take a look!')



# --------------------------------------------------------------------------------
# ## 3. Go and get some data from Spotify
# --------------------------------------------------------------------------------

# take a look at the spotify module that Sarah made:
from apis import spotify
help(spotify)



# --------------------------------------------------------------------------------
# ### Use the spotify.get_tracks() function to search for tracks
# --------------------------------------------------------------------------------

search_term = 'beyonce'
data = spotify.get_tracks(search_term)

# 3. write it to a file
file_path = get_file_path('results/' + search_term.replace(' ', '_') + '.json')
f = open(file_path, 'w')  
f.write(json.dumps(data))
f.close()


print('Spotify data written to', file_path)



# --------------------------------------------------------------------------------
# ## 3a. Go and get a Beyonce Song
# --------------------------------------------------------------------------------

# 1. get it from the internet
track_address = data[0]['preview_url']
track_id = data[0]['id']
print(track_address, track_id)
response = urlopen(track_address)
file_data = response.read()

# 2. print it to the screen
# print(file_data)

# 3. write it to a file
file_path = get_file_path('results/song_' + track_id + '.mp3')
f = open(file_path, 'wb')  #note the 'wb' flag (b is for binary)
f.write(file_data)
f.close()
print(file_path, 'Saved. Go take a look!')



# --------------------------------------------------------------------------------
# ### Display the tracks in a table
# --------------------------------------------------------------------------------

from IPython.core.display import HTML
HTML(spotify.get_formatted_tracklist_table_html(data))
album_id = data[0]['album']['id']
print(album_id)
HTML(spotify.get_album_player_html(album_id))



# --------------------------------------------------------------------------------
# ## 4. Go get some data from Yelp
# --------------------------------------------------------------------------------

from apis import yelp
help(yelp)
data = yelp.get_businesses()
# print(data[0])
HTML(yelp.get_formatted_business_table(data[0], reviews=[]))