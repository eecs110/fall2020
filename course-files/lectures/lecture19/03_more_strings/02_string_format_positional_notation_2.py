# Using positional notation:
template = '{0} is {1} years old.'

people = [
    ['Sally', 20],
    ['Rafael', 50],
    ['Dorcas', 61],
    ['Krista', 90]
]

for person in people:
    print(template.format(person[0], person[1]))  