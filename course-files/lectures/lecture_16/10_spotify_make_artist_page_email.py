import helpers
from apis import spotify
from apis import sendgrid

# Note: for email templates, you don't need the html document tags.
#       Use only the tags you'd need to create individual elements.
template = '''
    <h1>{artist_name}</h1>
    <p>More info <a href="{share_url}">here...</a></p>
    <img src="{image_url}" />
    {tracks_table}
'''

# Ask your user for input:
artist_name = input('What artist are you interested in? ')
from_email = input('What is your email? ')
to_emails = input('Who would you like to send the email to? ')
to_emails = to_emails.split(',')
message = input('What would you like to say to them about this playlist? ')

# go out and do the thing...
print('Retrieving Artist info...')
artist_data = spotify.get_artists(artist_name)
artist = artist_data[0]
tracks_data = spotify.get_top_tracks_by_artist(artist['id'])

# print(artist)
# print(tracks_data)
html_text = template.format(
    artist_name=artist['name'],
    image_url=artist['image_url_small'],
    share_url='share_url',
    tracks_table=spotify.get_formatted_tracklist_table_html(tracks_data)
)

print('Sending the email...')
sendgrid.send_mail(
    from_email=from_email,
    to_emails=to_emails,
    subject='Artist Profile (from Spotify)',
    html_content = message + '<br><br>' + html_text
)