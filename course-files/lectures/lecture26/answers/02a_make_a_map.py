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
lat = businesses[0].get('coordinates').get('latitude')
lng = businesses[0].get('coordinates').get('longitude')

# create map centered at first business retrieved:
map = folium.Map(
    location=[lat, lng],  #lat, lng
    zoom_start=13,
    tiles="Stamen watercolor"
)

# add marker at Shedd Aquarium:
# marker = folium.Marker(
#     location=[41.867226, -87.615355]
# )

for business in businesses:
    # print(business)
    lat = business.get('coordinates').get('latitude')
    lng = business.get('coordinates').get('longitude')
    if lat and lng:
        # print(lat, lng)
        marker = folium.Marker(
            location=[lat, lng],
            popup=business.get('name')
        )
        marker.add_to(map)


# show map:
map.save(get_file_path('my_map.html', subdirectory='results'))