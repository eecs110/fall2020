# pip3 install faker
# good for generating fake data
from faker import Faker
import random

f = Faker()
# print(dir(f))

# lets "generate" some fake people

def get_sponsor_type(amount:int=25):
    if amount > 5000:
        return 'Platinum sponsor'
    elif amount > 2500:
        return 'Gold sponsor'
    elif amount > 1000:
        return 'Silver sponsor'
    elif amount > 500:
        return 'Bronze sponsor'
    else:
        return 'sponsor'

def generate_people(num_people):
    people = []
    for i in range(0, num_people):
        donation = random.randint(10, 5500)
        name = f.name()
        email = name.lower().replace(' ', '_') + '@gmail.com'
        person = [name, email, donation, get_sponsor_type(donation)]
        people.append(person)
    return people


group1 = generate_people(15)
group2 = generate_people(5)
group3 = generate_people(5)
print(group1)
print(group2)
print(group3)
print(',\n'.join([str(p) for p in group1]))

