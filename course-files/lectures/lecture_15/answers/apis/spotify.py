import urllib.request
from urllib.request import urlopen
import json
import pandas as pd
import collections
from apis import authentication, utilities

get_image_html = utilities.get_image_html
flatten_for_pandas = utilities.flatten_for_pandas
get_dataframe = utilities.get_dataframe
get_jupyter_styling = utilities.get_jupyter_styling

def get_genres():
    url = 'https://api.spotify.com/v1/recommendations/available-genre-seeds'
    data = _issue_get_request(url)
    return data['genres']

def get_genres_abridged():
    return [
        "alternative", "ambient", "blues", 
        "chill", "country", "dance", "electronic", "folk", 
        "funk", "happy", "hip-hop", "indie-pop", "jazz", "k-pop", "metal", 
        "new-release", "pop", "punk", "reggae", "rock",
        "soul", "study", "trance", "work-out", "world-music"
    ]

def get_tracks(search_term:str, simplify:bool=True):
    '''
    Retrieves a list of Spotify tracks, given the search term passed in.
        * search_term (str): [Required] A search term (for a song), represented as a string.
        * simplify (bool):   Indicates whether you want to simplify the data that is returned.
    Returns a list of tracks.
    '''
    search_term = urllib.parse.quote_plus(search_term)
    url = 'https://api.spotify.com/v1/search?q=' + search_term + '&type=track'
    data = _issue_get_request(url)
    if not simplify:
        return data
    return _simplify_tracks(data['tracks']['items'])

def get_top_tracks_by_artist(artist_id:str, simplify:bool=True):
    '''
    Retrieves a list of Spotify "top tracks" by an artist
        * artist_id (str): [Required] The Spotify id of the artist.
        * simplify (bool):   Indicates whether you want to simplify the data that is returned.
    Returns a list of tracks.
    '''
    url = 'https://api.spotify.com/v1/artists/' + artist_id + '/top-tracks?country=us'
    # print(url)
    data = _issue_get_request(url)
    if not simplify:
        return data
    return _simplify_tracks(data['tracks'])

def get_tracks_by_playlist(playlist_id:str, simplify:bool=True):
    '''
    Retrieves a list of the tracks associated with a playlist_id
        * playlist_id (str): [Required] The id of the Spotify playlist.
        * simplify (bool):   Whether you want to simplify the data that is returned.
    Returns a list of tracks.
    '''
    url = 'https://api.spotify.com/v1/playlists/' + playlist_id + '/tracks'
    # print(url)
    data = _issue_get_request(url)
    if not simplify:
        return data
    
    def get_track(item):
        return item['track']
    tracks = list(map(get_track, data['items']))
    return _simplify_tracks(tracks)

def get_related_artists(artist_id:str, simplify:bool=True):
    '''
    Retrieves a list of artists related to the artist you specify
        * artist_id (str): [Required] The Spotify id of the artist, represented as a string.
        * simplify (bool):   Indicates whether you want to simplify the data that is returned.
    Returns a list of artists.
    '''
    url = 'https://api.spotify.com/v1/artists/' + artist_id + '/related-artists'
    # print(url)
    data = _issue_get_request(url)
    if not simplify:
        return data
    return _simplify_artists(data['artists'])

def get_artists(search_term:str, simplify:bool=True):
    '''
    Retrieves a list of Spotify artists, given the search term passed in.
        * search_term (str): [Required] A search term (for an artist), represented as a string.
        * simplify (bool):   Indicates whether you want to simplify the data that is returned.
    Returns a list of artists.
    '''
    search_term = urllib.parse.quote_plus(search_term)
    url = 'https://api.spotify.com/v1/search?q=' + search_term + '&type=artist'
    data = _issue_get_request(url)
    if not simplify:
        return data
    return _simplify_artists(data['artists']['items'])

def get_playlists(search_term:str, simplify:bool=True):
    '''
    Retrieves a list of Spotify tracks, given the search term passed in.
        * search_term (str): [Required] A search term (for a song), represented as a string.
        * simplify (bool):   Indicates whether you want to simplify the data that is returned.
    Returns a list of tracks.
    '''
    search_term = urllib.parse.quote_plus(search_term)
    url = 'https://api.spotify.com/v1/search?q=' + search_term + '&type=playlist'
    data = _issue_get_request(url)
    if not simplify:
        return data
    return _simplify_playlists(data['playlists']['items'])

def get_playlists_by_user(user_id:str, simplify:bool=True):
    '''
    Retrieves a list of Spotify tracks, given the search term passed in.
        * search_term (str): [Required] A search term (for a song), represented as a string.
        * simplify (bool):   Indicates whether you want to simplify the data that is returned.
    Returns a list of tracks.
    '''
    url = 'https://api.spotify.com/v1/users/' + user_id + '/playlists'
    data = _issue_get_request(url)
    if not simplify:
        return data
    return _simplify_playlists(data['items'])

def get_audio_features_by_track(track_id:str):
    '''
    Retrieves Spotify's audio analysis of the track.
        * track_id (str): [Required] The id of the Spotify track.
    Returns a list of audio features.
    '''
    url = 'https://api.spotify.com/v1/audio-features/' + track_id
    return _issue_get_request(url)

def get_similar_tracks(artist_ids:list=[], track_ids:list=[], genres:list=[], simplify:bool=True): 
    '''
    Spotify's way of providing recommendations. One or more params is required: 
    artist_ids, track_ids, or genres. Up to 5 seed values may be provided in 
    any combination of seed_artists, seed_tracks and seed_genres. In other words:
    len(artist_ids) + len(track_ids) + len(genres) between 1 and 5.
        * artist_ids (list): A list of artist ids
        * track_ids (list): A list of track ids
        * genres (genres): A list of genres
    Returns a list of tracks that are similar
    '''
    if not artist_ids and not track_ids and not genres:
        raise Exception('Either artist_ids or track_ids or genres required')
    
    # check if seeds <= 5:
    artist_ids = artist_ids or []
    track_ids = track_ids or []
    genres = genres or []
    if len(artist_ids) + len(track_ids) + len(genres) > 5:
        error = 'You can only have 5 "seed values" in your recommendations query.\n' + \
            'In other words, (len(artist_ids) + len(track_ids) + len(genres)) must be less than or equal to 5.'
        raise Exception(error)
    
    params = []
    if artist_ids:
        params.append('seed_artists=' + ','.join(artist_ids))
    if track_ids:
        params.append('seed_tracks=' + ','.join(track_ids))
    if genres:
        params.append('seed_genres=' + ','.join(genres))
    
    url = 'https://api.spotify.com/v1/recommendations?' + '&'.join(params)
    print(url)
    data = _issue_get_request(url)
    if not simplify:
        return data

    return _simplify_tracks(data['tracks'])


#############################
# Some formatting utilities #
#############################

def get_track_player_html(track_id:int):
    '''
    Creates the HTML tags for a Spotify player.
        * track_id (int): [Required] The id of a track.
    Returns an HTML iFrame  (str) corresponding to a Spotify player for the track. 
    '''
    return '''
    <iframe src="https://open.spotify.com/embed?uri=spotify:track:{track_id}&amp;theme=white" width="300" height="80" frameborder="0" allowtransparency="true" allow="encrypted-media" data-testid="audio-player">
    </iframe>
    '''.format(track_id=track_id)

def get_playlist_player_html(playlist_id:int, width:int=400, height:int=280):
    return '''
    <iframe src="https://open.spotify.com/embed/playlist/{playlist_id}" 
        width="{width}" height="{height}" frameborder="0" allowtransparency="true" 
        allow="encrypted-media">
    </iframe>'''.format(playlist_id=playlist_id, width=width, height=height)

def get_album_player_html(album_id:int, width:int=300, height:int=380):
    return '''
    <iframe src="https://open.spotify.com/embed/album/{album_id}" 
        width="{width}" height="{height}" frameborder="0" allowtransparency="true" 
        allow="encrypted-media">
    </iframe>'''.format(album_id=album_id, width=width, height=height)

def get_formatted_tracklist_table_html(tracks:list):
    '''
    Makes a nice formatted HTML table of tracks. Good for writing to an 
    HTML file or for sending in an email.
        * tracks(list): [Required] A list of tracks
    Returns an HTML table as a string 
    '''
    if not tracks:
        print('A list of tracks is required.')
        return
    flattened_data = flatten_for_pandas(tracks)
    pd.set_option('display.max_colwidth', -1)
    df = get_dataframe(flattened_data)
    keys = ['name', 'album_image_url_small', 'artist_name', 'album_name', 'share_url']
    df = df[keys]
    
    def image_formatter(im):
        return f'<img src="{im}" />'
    formatters={
        'album_image_url_small': image_formatter
    }
    playlist_table = df.to_html(formatters=formatters, escape=False, index=False)
    playlist_table = playlist_table.replace('style="text-align: right;"', '')
    playlist_table = playlist_table.replace('<tr>', '<tr style="border: solid 1px #CCC;">')
    playlist_table = playlist_table.replace(
        '<table border="1" class="dataframe">', 
        '<table style="border-collapse: collapse; border: solid 1px #CCC;">'
    )
    return playlist_table


############################################
# Some private, helper functions utilities #
############################################
# retrieves data from any Spotify endpoint:
def _issue_get_request(url):
    token = authentication.get_token('https://www.apitutor.org/spotify/key')
    request = urllib.request.Request(url, None, {
        'Authorization': 'Bearer ' + token
    })
    try:
        with urllib.request.urlopen(request) as response:
            data = json.loads(response.read().decode())
            return data
    except urllib.error.HTTPError as e:
        # give a good error message:
        error = utilities.get_error_message(e, url)
    raise Exception(error)

def _simplify_tracks(tracks:list):
    try:
        tracks[0]
    except Exception:
        return tracks

    simplified = []
    # print(tracks[0])
    for item in tracks:
        track = { 
            'id': item['id'], 
            'name': item['name'], 
            'preview_url': item['preview_url'],
            'share_url': 'https://open.spotify.com/track/' + item['id']
        }
        try:
            track['album'] = {
                'id': item['album']['id'],
                'name': item['album']['name'],
                'image_url': item['album']['images'][0]['url'],
                'image_url_small': item['album']['images'][-1]['url'],
                'share_url': 'https://open.spotify.com/album/' + item['album']['id']
            }
        except Exception:
            pass
        try:
            artists = item.get('album').get('artists')
            artist = artists[0]
            track['artist'] = { 
                'id': artist['id'], 
                'name': artist['name'],
                'share_url': 'https://open.spotify.com/artist/' + item['album']['artists'][0]['id']
            }
        except Exception:
           pass
        simplified.append(track)
    return simplified

def _simplify_artists(artists:list):
    try:
        artists[0]
    except Exception:
        return artists

    simplified = []
    for item in artists:
        artist = { 
            'id': item['id'], 
            'name': item['name'], 
            'genres': ', '.join(item['genres']),
            'share_url': 'https://open.spotify.com/artist/' + item['id']
        }
        try:
            artist['image_url'] = item['images'][0]['url']
            artist['image_url_small'] = item['images'][-1]['url']
        except Exception:
            pass
        simplified.append(artist)
    return simplified

def _simplify_playlists(playlists:list):
    try:
        simplified = []
        for item in playlists:
            simplified.append({ 
                'id': item['id'], 
                'name': item['name'], 
                'owner_display_name': item['owner']['display_name'],
                'owner_id': item['owner']['id'],
                'share_url': 'https://open.spotify.com/playlist/' + item['id']
            })
        return simplified
    except Exception as e:
        # give a good error message:
        error = 'The following playlist data structure could not be flattened:\n' + str(playlists)
        # print(error)
        raise Exception(error)