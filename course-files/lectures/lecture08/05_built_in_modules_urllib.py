from urllib.request import urlopen
import ssl

def get_file_path(file_name):
    import os
    import sys
    dir_path = os.path.dirname(sys.argv[0])
    return os.path.join(dir_path, file_name)


def save_image_from_internet(url):
    print('Retrieving data from...', url)
    context = ssl._create_unverified_context()    
    
    # retrieve the following file from the internet
    with urlopen(url, context=context) as response:
        data = response.read()
        
        # write Internet data to a file: 
        file_name = url.split('/')[-1]
        f = open(get_file_path(file_name), 'wb')
        f.write(data)
        f.close()


cat_photo_url = 'https://media.wired.com/photos/5cdefc28b2569892c06b2ae4/master/w_2560%2Cc_limit/Culture-Grumpy-Cat-487386121-2.jpg' 
save_image_from_internet(cat_photo_url)