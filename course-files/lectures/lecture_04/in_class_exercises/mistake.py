def area_of_square(length:int):
   return length * length

def surface_area_of_cube(area:int):
   area * 6

print(
   'Surface area of a cube where side=10 feet is:',
   surface_area_of_cube(area_of_square(10)),
   'feet'
)
