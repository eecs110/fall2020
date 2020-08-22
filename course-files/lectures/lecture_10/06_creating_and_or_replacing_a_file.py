import utilities
f = open(utilities.get_file_path('my_new_file.txt'), 'w', encoding='utf8')

f.write('hello world!')
f.close()