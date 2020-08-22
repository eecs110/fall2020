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
list_of_violations_by_restaurant = {}
for row in reader(f_violations):
    license = row[0]
    business_name = business_license_lookup.get(license)
    violation_text = row[3]
    if list_of_violations_by_restaurant.get(business_name) is None:
        # add a new element:
        list_of_violations_by_restaurant[business_name] = []
    list_of_violations_by_restaurant[business_name].append(violation_text)

# 3. sorting it:
items = list_of_violations_by_restaurant.items()
sorted_items = sorted(items, key=lambda key_value: len(key_value[1]), reverse=True)
for item in sorted_items:
    violations = item[1]
    if len(violations) > 15:
        print('*' * 88)
        print(item[0])
        print('*' * 88)
        for violation in violations:
            print('    *', violation[:80])
        print()
        print()