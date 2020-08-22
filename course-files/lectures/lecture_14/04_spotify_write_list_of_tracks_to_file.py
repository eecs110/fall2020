
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
# 1. Send someone an email where the track_table_html is in the body of the email.

# 2. Create an HTML file that lists all of the tracks
# in a table using the spotify.get_formatted_tracklist_table_html



