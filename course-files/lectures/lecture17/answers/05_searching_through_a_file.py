import utilities
f = open(utilities.get_file_path('moby_dick.txt'), 'r', encoding='utf8')

count = 0
for line in f:
    words = line.split(' ')
    for word in words:
        if word.upper() == 'MOBY':
            count += 1
            # print(line)

print('Moby appears ', count, 'times in the file.')