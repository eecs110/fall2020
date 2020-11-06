track = {
    "id": "5IVuqXILoxVWvWEPm82Jxr",
    "name": "Crazy In Love (feat. Jay-Z)",
    "preview_url": "https://p.scdn.co/mp3-preview/ce8ace0ec425840416be78db07cf50dd331eed4f?cid=9697a3a271d24deea38f8b7fbfa0e13c",
    "album": {
        "id": "6oxVabMIqCMJRYN1GqR3Vf",
        "name": "Dangerously In Love",
        "image_url": "https://i.scdn.co/image/ab67616d0000b27345680a4a57c97894490a01c1"
    },
    "artist": {
        "id": "6vWDO969PvNqNYHIOW5v0m",
        "name": "Beyoncé"
    }
}

'''
Given the dictionary above...

1. How many keys does the track dictionary have?
2. What type of data is stored inside of...
    The "id" slot?
    The "name" slot?
    The "preview_url" slot?
    The "album" slot?
    The "artist" slot?
3. How do I print the name of the track?
4. How do I print the name of the album?
5. How do I print the name of the artist?
'''

print('\nPart 1.')
print(track.keys())
print('There are', len(track.keys()), 'keys in the track dictionary.')

print('\nPart 2.')
# recommended to use the "get" method:
print('a.', track.get('id'), type(track.get('id')))
print('a.', track['id'], type(track['id']))

print('b.', track.get('name'), type(track.get('name')))

print('c.', track.get('preview_url'), type(track.get('preview_url')))

print('d.', track.get('album'), type(track.get('album')))

print('e.', track.get('artist'), type(track.get('artist')))

print('\nPart 3.')
print(track.get('name'))

print('\nPart 4.')
album = track.get('album')
print(album.get('name'))
# or:
print(track.get('album').get('name'))

print('\nPart 5.')
artist = track.get('artist')
# or:
print(artist.get('name'))
print(track.get('artist').get('name'))