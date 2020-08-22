'''
You're working for the city and want to identify all of the senior
citizens in your district to send out a mailer -- as they may qualify
for a special tax waiver. You are given a (messy and incomplete) data
set. Your boss wants you to create 2 files:

  * One for people with a complete data profile (no obvious mistakes)
  * One for people with an incomplete / suspect data profile

Write a program to do this.
'''

import utilities
f_source = open(utilities.get_file_path('people.csv'), 'r')
f_valid = open(utilities.get_file_path('people_valid.csv'), 'w')
f_invalid = open(utilities.get_file_path('people_invalid.csv'), 'w')

for line in f_source.readlines()[1:]:
    cells = line.split(',')
    name = cells[0]
    age = cells[1]
    address = cells[2]

    if len(cells) != 3:
        f_invalid.write(line)
        continue
    
    try:
        age = int(age)
    except:
        f_invalid.write(line)
        continue

    if age < 0 or age > 120:
        f_invalid.write(line)
        continue
    
    f_valid.write(line)

f_source.close()
f_valid.close()
f_invalid.close()