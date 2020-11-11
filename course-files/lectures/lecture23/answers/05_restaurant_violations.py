# write a program that reads the contents of the Food_Establishment_Violations
# for the City of Evanston and counts the number of violations that have occurred
# for each restaurant code. The, print out the restaurant code and the number of violations

# VS Code Hack:
import sys
import os
from csv import reader
dir_path = os.path.dirname(sys.argv[0])

# 1. start by creating a lookup table where 
# the key is the business license
# and the value is the name of the business
business_license_lookup = {}
file_path = os.path.join(dir_path, 'Food_Establishment_Businesses.csv')
f_businesses = open(file_path, 'r', encoding='utf8', errors='ignore')
for row in reader(f_businesses):
    business_license_lookup[row[0]] = row[1]


# 2. opened the violations file:
file_path = os.path.join(dir_path, 'Food_Establishment_Violations.csv')
f_violations = open(file_path, 'r', encoding='utf8', errors='ignore')
counts_dict = {}
for row in reader(f_violations):
    license = row[0]
    business_name = business_license_lookup.get(license)
    if counts_dict.get(business_name) is None:
        # add a new element:
        counts_dict[business_name] = 1
    else:
        counts_dict[business_name] += 1

# 3. sorting it:
from operator import itemgetter # import itemgetter; use it to access value
items = counts_dict.items()
sorted_items = sorted(items, key=itemgetter(1), reverse=True)
for item in sorted_items:
    print(item[1], '-', item[0])


# 4. Formatting Added:
# template = '{0:12}  {1}'
# print()
# print('-' * 60)
# print(template.format('# Violations', 'Restaurant Name'))
# print('-' * 60)
# for item in sorted_items:
#     # only show if more than 15 violations:
#     if item[1] > 15:
#         print(template.format(item[1], item[0]))
# print('-' * 60)