
from urllib.request import urlopen
import pprint
import json
import pandas as pd
from apis import spotify

def get_file_path(file_name, subdirectory=None):
    import os
    import sys
    dir_path = os.path.dirname(sys.argv[0])
    if subdirectory:
        return os.path.join(dir_path, subdirectory, file_name)
    else:
        return os.path.join(dir_path, file_name)

# Go and get tracks
search_term = input('Enter your search term: ')
data = spotify.get_tracks(search_term)

album_id = data[0]['album']['id']
album_name = data[0]['album']['name']
player = spotify.get_album_player_html(album_id)

# See files from Lecture 11
template = '''
<html>
    <head>
        <title>{album_name}</title>
    </head>
    <body>
        <h1>{album_name}</h1>
        {player}
    </body>
</html>
'''

# YOUR TASK:
# Create an HTML file with a spotify album player
# using the spotify.get_album_player_html
html = template.format(
    album_name=album_name,
    player=player
)

file_path = get_file_path(search_term.replace(' ', '_') + '_player.html', subdirectory='results')
f = open(file_path, 'w')
f.write(html)
f.close()

