import urllib.request
import json
import ssl
import pprint

# Write a program that only prints the text of the most popular 
# tweet (given the search results).

# necessary for accessing data via https protocol:

# search for tracks: https://www.apitutor.org/spotify/simple/v1/search?type=track&q=beyonce
# search for artists: https://www.apitutor.org/spotify/simple/v1/search?type=artist&q=beyonce
# search albums: https://www.apitutor.org/spotify/simple/v1/search?type=album&q=beyonce
context = ssl._create_unverified_context()

search_term = input('Please enter a search term: ')

url = 'https://www.apitutor.org/spotify/simple/v1/search?type=track&q='
url += search_term
print(url)
response = urllib.request.urlopen(url, context=context)
statuses = json.loads(response.read().decode())

pprint.pprint(statuses, depth=2) # The first value is another dictionary, the second is a list of dictionaries