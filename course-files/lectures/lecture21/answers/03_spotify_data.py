import urllib.request
import json
import ssl
import pprint

# Write a program that only prints the text of the most popular 
# tweet (given the search results).

# necessary for accessing data via https protocol:

# search for tracks: https://www.apitutor.org/spotify/simple/v1/search?type=track&q=beyonce
# search for artists: https://www.apitutor.org/spotify/simple/v1/search?type=artist&q=beyonce
# search albums: https://www.apitutor.org/spotify/simple/v1/search?type=album&q=beyonce


def search_for_tracks(search_term:str):
    search_term = search_term.replace(' ', '%20')
    context = ssl._create_unverified_context()
    # create query url:
    url = 'https://www.apitutor.org/spotify/simple/v1/search?type=track&q=' + search_term

    # retrieve the data:
    response = urllib.request.urlopen(url, context=context)
    return json.loads(response.read().decode())

term = input('Enter a search term to look for some tracks: ')
tracks = search_for_tracks(term)

for track in tracks:
    print(track.get('name'), '(' + track.get('artist').get('name') + ')')