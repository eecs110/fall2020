#example: print all keys and values one by one:
import json
import utilities


playlist = []
try:
    # open playlist file if it exists and update playlist
    f = open(utilities.get_file_path('playlist.json'), 'r')
    playlist = json.loads(f.read())
    f.close()
except Exception:
    # if there's an error, just keep the existing playlist
    pass


template = '{0:<20}{1:<40}{2:<10}{3:<10}'
print('-' * 80)
print(template.format('Artist', 'Song', 'Genre', 'Year'))
print('-' * 80)
for track in playlist:
    print(
        template.format(
            track.get('artist_name'),
            track.get('song_name'),
            track.get('genre'),
            track.get('year')
        )
    )
print('-' * 80)