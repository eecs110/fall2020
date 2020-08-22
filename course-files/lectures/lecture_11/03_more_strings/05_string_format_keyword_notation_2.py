# Using positional notation:
template = '{name} is {age} years old.'

people = [
    ['Sally', 20],
    ['Rafael', 50],
    ['Dorcas', 61],
    ['Krista', 90]
]

for person in people:
    print(template.format(name=person[0], age=person[1]))  