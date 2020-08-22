# pip3 install faker
# good for generating fake data
from faker import Faker

f = Faker()
# print(dir(f))

# lets "generate" some fake people
def generate_people(num_people):
    people = []
    for i in range(0, num_people):
        person = [i, f.name(), f.street_address(), f.city(), f.state(), f.zipcode(), f.job()]
        people.append(person)
    return people


group1 = generate_people(5)
group2 = generate_people(5)
group3 = generate_people(5)
print(group1)
print(group2)
print(group3)
# print(',\n'.join([str(p) for p in people]))

