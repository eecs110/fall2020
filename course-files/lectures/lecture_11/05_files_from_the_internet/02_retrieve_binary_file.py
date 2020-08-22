import utilities
import ssl # for https requests
from urllib.request import urlopen

items = [
    ('https://kittenrescue.org/wp-content/uploads/2017/03/KittenRescue_KittenCareHandbook.jpg', 'kitten.jpg'),
    ('https://p.scdn.co/mp3-preview/9e37f230afd37042e49f3d144c3b94e0b39ef8ba?cid=9697a3a271d24deea38f8b7fbfa0e13c', 'eye_of_the_tiger.mp3')
]

for item in items:
    url = item[0]
    file_name = item[1]
    # 1. get it from the internet
    context = ssl._create_unverified_context()
    response = urlopen(url, context=context)
    file_data = response.read()

    # 2. print it to the screen
    # print(file_data)

    # 3. write it to a file
    file_path = utilities.get_file_path(file_name, subdirectory='results')
    f = open(file_path, 'wb')  #note the 'wb' flag (b is for binary)
    f.write(file_data)
    f.close()
    print('Binary file written to', file_path, '\nGo take a look!')