import utilities
source_file = open(utilities.get_file_path('moby_dick.txt'), 'r', encoding='utf8')
destination_file = open(utilities.get_file_path('moby_dick_line_numbers.txt'), 'w', encoding='utf8')

linenum = 1
for line in source_file:
    destination_file.write(str(linenum) + '. ')
    destination_file.write(line)
    linenum += 1
source_file.close()
destination_file.close()