from csv import reader
# write a program that reads the contents of the Food_Establishment_Violations
# for the City of Evanston and counts the number of violations that have occurred
# for each restaurant code. The, print out the restaurant code and the number of violations

def get_file_path(file_name, subdirectory=None):
    import os
    import sys
    dir_path = os.path.dirname(sys.argv[0])
    if subdirectory:
        return os.path.join(dir_path, subdirectory, file_name)
    else:
        return os.path.join(dir_path, file_name)

def sort_dictionary(d:dict):
    # Helper function to sort a dictionary
    import collections
    return collections.OrderedDict(
        sorted(d.items(), key=lambda kv: -1 * kv[1])
    )

file_path = get_file_path('Trees_data.csv')
f = open(file_path, 'r', encoding='utf8', errors='ignore')
rows = list(reader(f))

# let's print all of the column headers:
header = rows[0]

i = 0
for cell in header:
    print(i, '->', cell)
    i += 1

types_of_trees = {}
for row in rows[1:]:
    common_name = row[39].replace('"', '').lower()
    condition = row[16].replace('\n', '').lower()
    if common_name in types_of_trees:
        # add one to existing entry:
        types_of_trees[common_name] += 1
    else:
        # add new entry to the dictionary:
        types_of_trees[common_name] = 1

types_of_trees_sorted = sort_dictionary(types_of_trees)
for key in types_of_trees_sorted:
    print(types_of_trees_sorted[key], '\t', key)