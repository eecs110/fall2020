import utilities
f = open(utilities.get_file_path('my_new_file.txt'), 'a', encoding='utf8')

f.write('\nthis is another line. It will append to my_file.txt')
f.close()