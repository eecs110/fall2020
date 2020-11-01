import utilities
import ssl # for https requests
from urllib.request import urlopen


# 1. get it from the internet
context = ssl._create_unverified_context()
response = urlopen('https://www.google.com', context=context)
file_data = response.read().decode('utf-8', 'ignore')

# 2. print it to the screen
print(file_data)

# 3. write it to a file
file_path = utilities.get_file_path('google_homepage.html', subdirectory='results')
f = open(file_path, 'w')
f.write(file_data)
f.close()
print('Web page written to results/google_homepage.html. Go take a look!')