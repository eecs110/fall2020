import utilities

template = '''
    <html>
        <head><title>{name}</title></head>
        <body>
            <h1>{name}</h1>
            <p>Listen on <a href="{link}">Spotify</a></p>
            <img style="width: 400px;" src="{image}" />
        </body>
    </html>
'''
artists = [
    ['Beyonce', 'https://i.scdn.co/image/9fef2047e4e3f05031807d5fa9e121b7862ba259', 'https://open.spotify.com/artist/6vWDO969PvNqNYHIOW5v0m'],
    ['The Rolling Stones', 'https://i.scdn.co/image/85d9cb252ab4d8410d31820be40214c59f2597a1', 'https://open.spotify.com/artist/22bE4uQ6baNwSHPVcDxLCe'],
    ['Madonna', 'https://i.scdn.co/image/96b4818a65820e91e0e17fcf55a4d2213b019ad4', 'https://open.spotify.com/artist/6tbjWDEIzxoDsBA1FuhfPW'],
]

for artist in artists:
    artist_name = artist[0]
    artist_image = artist[1]
    artist_url = artist[2]
    file_name = artist_name.replace(' ', '_').lower() + '.html'
    html_text = template.format(name=artist_name, image=artist_image, link=artist_url)
    file_path = utilities.get_file_path(file_name, subdirectory='results')
    f = open(file_path, 'w')
    f.write(html_text)
    f.close()