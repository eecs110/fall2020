import utilities

# Challenge: using the template defined for you below, 
# create an HTML for each artist in the artists list below

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
