import utilities
f = open(utilities.get_file_path('moby_dick.txt'), 'r', encoding='utf8')

counter = 0
for line in f:
    words = line.split(' ')
    counter += len(words)


print('there are ', counter, 'words in the file.')