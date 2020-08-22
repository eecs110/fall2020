from csv import reader
# write a program that reads the contents of the Trees_data.csv file
# to find out the number of trees in each health category...

# Next week: we're going to make a map of them!

# VS Code Hack:
import sys
import os
dir_path = os.path.dirname(sys.argv[0])
file_path = os.path.join(dir_path, 'data', 'Trees_data.csv')
# End VS Code Hack:

def sort_dictionary(d:dict):
    import collections
    return collections.OrderedDict(
        sorted(d.items(), key=lambda kv: -1 * kv[1])
    )


f = open(file_path, 'r', encoding='utf8', errors='ignore')
rows = list(reader(f))

# let's print all of the column headers:
header = rows[0]
i = 0
for cell in header:
    print(i, '->', cell)
    i += 1

condition_dict = {}
for row in rows[1:]:
    condition = row[16].replace('\n', '').lower()
    common_name = row[39].replace('"', '').lower()
    # print(condition)
    if condition in condition_dict:
        # add one to existing entry:
        condition_dict[condition] += 1
    else:
        # add new entry to the dictionary:
        condition_dict[condition] = 1

condition_dict_sorted = sort_dictionary(condition_dict)
for key in condition_dict:
    print(key, '->', condition_dict[key])

print(condition_dict.get('poor'))