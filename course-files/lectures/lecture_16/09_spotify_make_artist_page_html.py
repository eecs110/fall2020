import helpers
from apis import spotify

template = '''
    <html>
        <head>
            <title>{artist_name}</title>
            <style>
                body {{ 
                    font-family: Arial; 
                    margin: 30px 100px 30px 100px;
                }}
                table {{ margin-top: 20px;}}
            </style>
        </head>
        <body>
            <h1>{artist_name}</h1>
            <p>More info <a href="{share_url}">here...</a></p>
            <img src="{image_url}" />
            {tracks_table}
        </body>
    </html>
'''

artist_data = spotify.get_artists('beyonce')
artist = artist_data[0]
tracks_data = spotify.get_top_tracks_by_artist(artist['id'])
tracks_table = spotify.get_formatted_tracklist_table_html(tracks_data)


# print(artist)
# print(tracks_data)
html_text = template.format(
    artist_name=artist['name'],
    image_url=artist['image_url_small'],
    share_url='share_url',
    tracks_table=tracks_table
)

file_path = helpers.get_file_path('beyonce.html', subdirectory='results')
f = open(file_path, 'w')
f.write(html_text)
f.close()