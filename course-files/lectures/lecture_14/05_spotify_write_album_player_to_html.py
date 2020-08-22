
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

# how do you use:
# spotify.get_album_player_html(???)

# See files from Lecture 11
html_template = '''
<html>
    <head>
        <title>Tracks</title>
    </head>
    <body>
        <h1>Header</h1>
        <p>Some text</p>
    </body>
</html>
'''

# YOUR TASK:
# Create an HTML file with a spotify album player
# using the spotify.get_album_player_html

