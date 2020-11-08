import urllib.request
import utilities
import json
import ssl

def search_for_tracks(search_term:str):
    search_term = search_term.replace(' ', '%20')
    context = ssl._create_unverified_context()
    # create query url:
    url = 'https://www.apitutor.org/spotify/simple/v1/search?type=track&q=' + search_term

    # connect to the server at the given address:
    response = urllib.request.urlopen(url, context=context)
    
    # download the corresponding data and 
    # load it into a list of dictionaries: 
    return json.loads(response.read().decode())

# Your job:
# How do you download some album covers from the tracks data?
term = input('Enter a search term to look for some tracks: ')
tracks = search_for_tracks(term)

for track in tracks:
    print(track.get('album').get('name'), track.get('album').get('image_url'))