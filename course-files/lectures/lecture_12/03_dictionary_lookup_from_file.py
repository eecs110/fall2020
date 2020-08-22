import json
import utilities

# 1. read lookup table from a file:
f = open(utilities.get_file_path('state_capitals.json'), 'r')

# 2. conveniance function that converts text from 
#    a JSON file into dictionary:
capital_lookup = json.loads(f.read())

# 3. Then access the dictionary:
print('You can also load a dictionary from a file!')
print('The capital of Florida is:', capital_lookup.get('Florida'))
print('The capital of Illinois is:', capital_lookup.get('Illinois'))
print('The capital of California is:', capital_lookup.get('California'))
print('The capital of Massachusetts is:', capital_lookup.get('Massachusetts'))