import my_module

print('Area:', my_module.get_area(32, 23))
print('Perimeter:', my_module.get_perimeter(32, 23))
print('Hypotenuse:', my_module.get_hypotenuse(32, 23))


my_module.print_to_2_decimal_places(my_module.get_area(32, 23))
my_module.print_to_2_decimal_places(my_module.get_perimeter(32, 23))
my_module.print_to_2_decimal_places(my_module.get_hypotenuse(32, 23))