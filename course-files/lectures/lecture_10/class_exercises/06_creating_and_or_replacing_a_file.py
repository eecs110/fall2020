import utilities
file_path = utilities.get_file_path('thursday_lecture.txt')
f = open(file_path, 'a', encoding='utf8')
f.write('\nTest')
f.close()