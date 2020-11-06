import urllib.request
import utilities
import json
import ssl

# How do you download some album covers from the tracks data?
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
    print(track.get('album').get('name'), track.get('album').get('image_url'))