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
    print('There was an error loading your file...')
    pass


################################################################
# YOUR JOB: 
#    Print the entire playlist to the screen in a way that makes
#    sense...
################################################################