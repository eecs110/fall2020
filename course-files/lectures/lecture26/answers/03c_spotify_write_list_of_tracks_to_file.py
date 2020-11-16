
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

# Display the tracks in a table

track_table_html = spotify.get_formatted_tracklist_table_html(data)

template = '''<html>
    <head>
        <title>Spotify Search</title>
    </head>
    <body>
        <h1>{search_term}</h1>
        <p>The following tracks matched your search term:</p>
        {track_table_html}
    </body>
</html>'''

html = template.format(
    search_term=search_term, 
    track_table_html=track_table_html
)

file_path = get_file_path(search_term.replace(' ', '_') + '.html', subdirectory='results')
f = open(file_path, 'w')
f.write(html)
f.close()


# album_id = data[0]['album']['id']
# print(album_id)
# album_player_html = spotify.get_album_player_html(album_id)
# print(album_player_html)
