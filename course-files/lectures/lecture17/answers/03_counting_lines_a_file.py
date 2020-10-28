import utilities
f = open(utilities.get_file_path('moby_dick.txt'), 'r', encoding='utf8')

counter = 0
for line in f:
    counter += 1

print('there are ', counter, 'lines in the file.')