import urllib.request
import utilities
import ssl

# How do you download some sample audio from the tracks data?

# location of audio file:
url_address_peace_of_mind = 'https://p.scdn.co/mp3-preview/7ea00cefb82b042c644cf5447a0d78f2d7546fd7?cid=9697a3a271d24deea38f8b7fbfa0e13c'

# retrieve the data and save the data in a file_data variable:
context = ssl._create_unverified_context()
response = urllib.request.urlopen(url_address_peace_of_mind, context=context)
file_data = response.read()

# create a local file with the 'wb' flag
local_path = utilities.get_file_path('peace_of_mind.mp3')
f = open(local_path, 'wb')
f.write(file_data)
f.close()
