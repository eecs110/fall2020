import utilities
f = open(utilities.get_file_path('my_new_file.txt'), 'a', encoding='utf8')

colors = ['red', 'pink', 'purple', 'orange', 'teal', 'blue']
for color in colors:
    f.write(color)
    f.write('\n')

f.close()