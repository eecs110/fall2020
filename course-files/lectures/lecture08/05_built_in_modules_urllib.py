from urllib.request import urlopen
import ssl


def get_file_path(file_name):
    import os
    import sys
    dir_path = os.path.dirname(sys.argv[0])
    return os.path.join(dir_path, file_name)

context = ssl._create_unverified_context()

# replace with address of any image:
cat_photo_url = 'https://media.wired.com/photos/5cdefc28b2569892c06b2ae4/master/w_2560%2Cc_limit/Culture-Grumpy-Cat-487386121-2.jpg' 

print('Retrieving data from...', cat_photo_url)
with urlopen(cat_photo_url, context=context) as response:
   data = response.read()
   # write to file: 
   f = open(get_file_path('cat.jpg'), 'wb')
   f.write(data)
   f.close()