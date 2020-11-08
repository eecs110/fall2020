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
    song_name = input('Album Name: ')
    genre = input('Genre: ')
    ################################################################
    # YOUR JOB: 
    #    Write some code that stores this user-generated information
    #    and appends it to the current playlist...
    ################################################################
    






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