
from urllib.request import urlopen
import pprint
import json
from apis import spotify

def get_file_path(file_name, subdirectory=None):
    import os
    import sys
    dir_path = os.path.dirname(sys.argv[0])
    if subdirectory:
        return os.path.join(dir_path, subdirectory, file_name)
    else:
        return os.path.join(dir_path, file_name)

# take a look at the spotify module that Sarah made...
from apis import spotify
help(spotify)
# ...and press "Q" to exit the help

# 1. Use the spotify.get_tracks(...) function to search for tracks
search_term = 'beyonce'
data = spotify.get_tracks(search_term)

# 3. write all of the JSON data (i.e. list of dictionaries) to a file
file_path = get_file_path(search_term.replace(' ', '_') + '.json', subdirectory='results')
f = open(file_path, 'w')  
f.write(json.dumps(data))
f.close()
print('Spotify data written to', file_path)


# YOUR TASK:
# Go and download all of the mp3s from spotify 
# (note: only 30 second previews are available)


