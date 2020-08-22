from csv import reader

# write a program that reads the contents of the Trees_data.csv file
# to find out the number of trees of each species...

# Next week: we're going to map them.
def get_file_path(file_name, subdirectory=None):
    import os
    import sys
    dir_path = os.path.dirname(sys.argv[0])
    if subdirectory:
        return os.path.join(dir_path, subdirectory, file_name)
    else:
        return os.path.join(dir_path, file_name)


def sort_dictionary(d:dict):
    import collections
    return collections.OrderedDict(
        sorted(d.items(), key=lambda kv: -1 * kv[1])
    )

file_path = get_file_path('Trees_data.csv', subdirectory='data')
f = open(file_path, 'r', encoding='utf8', errors='ignore')
rows = list(reader(f))

# print first 3 lines:
for row in rows[:3]:
    print(row)