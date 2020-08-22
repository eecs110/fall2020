
from urllib.request import urlopen
import pprint
import json
import pandas as pd
from apis import spotify
import time

def get_file_path(file_name, subdirectory=None):
    import os
    import sys
    dir_path = os.path.dirname(sys.argv[0])
    if subdirectory:
        return os.path.join(dir_path, subdirectory, file_name)
    else:
        return os.path.join(dir_path, file_name)


# 1. Use the spotify.get_tracks(...) function to search for tracks
search_term = 'beyonce'
data = spotify.get_tracks(search_term)

# 3. write all of the JSON data (i.e. list of dictionaries) to a file
file_path = get_file_path(search_term.replace(' ', '_') + '.json', subdirectory='results')
f = open(file_path, 'w')  
f.write(json.dumps(data))
f.close()
print('Spotify data written to', file_path)


# 3 Go and download all the Beyonce samples...

# 1. get it from the internet
for track in data:
    track_id = track.get('id')
    track_address = track.get('preview_url')
    
    if track_address is not None:
        print('Retrieving', track_address, '...')

        # go and get the binary song file from the web address...
        response = urlopen(track_address)
        file_data = response.read()

        # ...and write it to a file
        file_path = get_file_path('song_' + track_id + '.mp3', subdirectory='results')
        f = open(file_path, 'wb')  #note the 'wb' flag (b is for binary)
        f.write(file_data)
        f.close()

        # then be polite and sleep for 1 seconds so you don't overwhelm
        # Spotify's servers...
        time.sleep(1)