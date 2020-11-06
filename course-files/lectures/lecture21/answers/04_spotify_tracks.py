import urllib.request
import utilities
import json
import ssl
import time

# How do you download some sample audio from the tracks data?
def search_for_tracks(search_term:str):
    search_term = search_term.replace(' ', '%20')
    context = ssl._create_unverified_context()
    # create query url:
    url = 'https://www.apitutor.org/spotify/simple/v1/search?type=track&q=' + search_term

    # retrieve the data:
    response = urllib.request.urlopen(url, context=context)
    return json.loads(response.read().decode())

def save_track_to_disk(url:str, file_path:str):
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(url, context=context)
    file_data = response.read()

    # create a local file with the 'wb' flag
    f = open(file_path, 'wb')
    f.write(file_data)
    f.close()

term = input('Enter a search term to look for some tracks: ')
tracks = search_for_tracks(term)

for track in tracks:
    song_url = track.get('preview_url')
    if song_url is None:
        continue
    
    local_file_name = track.get('name').lower().replace(' ', '') + '.mp3'
    local_file_name = local_file_name.replace('/', '')
    local_file_name = local_file_name.replace('\'', '')

    # hack for VS code (not necessary in IDLE I don't think):
    local_file_path = utilities.get_file_path(local_file_name)
    print('Saving to:', local_file_name)
    save_track_to_disk(song_url, local_file_path)
    time.sleep(1)