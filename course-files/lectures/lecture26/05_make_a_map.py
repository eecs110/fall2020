# pip3 install folium

import folium
from apis import yelp

def get_file_path(file_name, subdirectory=None):
    import os
    import sys
    dir_path = os.path.dirname(sys.argv[0])
    if subdirectory:
        return os.path.join(dir_path, subdirectory, file_name)
    else:
        return os.path.join(dir_path, file_name)

businesses = yelp.get_businesses()

# create map:
map = folium.Map(
    location=[41.867226, -87.615355],  #lat, lng
    zoom_start=13,
    tiles="Stamen watercolor"
)

# add marker at Shedd Aquarium:
marker = folium.Marker(
    location=[41.867226, -87.615355],
    popup='Shedd Aquarium'
)
marker.add_to(map)



# show map:
map.save(get_file_path('my_map.html', subdirectory='results'))