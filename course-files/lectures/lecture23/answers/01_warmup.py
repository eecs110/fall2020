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


# Now, prompt the user for songs to add to her playlist:
while True:
    artist_name = input('Artist: ')
    song_name = input('Song Name: ')
    genre = input('Genre: ')
    tags = input('Tags: ')
    year = input('Year Released: ')
    # YOUR CODE HERE 

    playlist.append({
        'artist_name': artist_name,
        'song_name': song_name,
        'genre': genre,
        'tags': tags,
        'year': year
    })

    # END YOUR CODE HERE
    up_next = input('Do you want to add another track (Y/n)?' )
    if up_next.upper() == 'N':
        # Exit the loop...
        print('writing your tracks to the file...\n')
        break


# overwrite tracks.json with new track list:
f = open(utilities.get_file_path('playlist.json'), 'w')
f.write(json.dumps(playlist))
f.close()