import utilities

word = input('what word do you want to look for?')
word = word.lower()
counter = 1
f = open(utilities.get_file_path('moby_dick.txt'), 'r', encoding='utf8')
f_destination = open(utilities.get_file_path(word + '.txt'), 'a', encoding='utf8')

for line in f.readlines():
    # how many times does the word "Moby" appear?
    words = line.lower().split(' ')
    if word in words:  # is the word 'Moby' in any slot of the list?
        # print(counter, line)
        f_destination.write(str(counter) + '.  ' + line)
    counter += 1
f.close()
f_destination.close()


# print('Moby appears ', ?????, 'times in the file.')