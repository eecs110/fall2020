import utilities
f = open(utilities.get_file_path('moby_dick.txt'), 'r', encoding='utf8')

# Your job: can you write some code to see
# how many times the word "Moby" appears in
# the file?
for line in f:
    print(line)
f.close()

# print('Moby appears ', ?????, 'times in the file.')