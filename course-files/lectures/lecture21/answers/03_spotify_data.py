import urllib.request
import json
import ssl
import pprint

'''
1. Prompt the user for a search term 
2. Query the Spotify tracks endpoint for the search term
3. Print the song name and the artist(s) who wrote it. 
'''

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