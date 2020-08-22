import right_triangles


side_a = float(input('Enter your first side: '))
side_b = float(input('Enter your second side: '))

area = right_triangles.get_area(side_a, side_b)
print(area)

hypotenuse = right_triangles.get_hypotenuse(side_a, side_b)
print(hypotenuse)

perimeter = right_triangles.get_perimeter(side_a, side_b)
print(perimeter)

