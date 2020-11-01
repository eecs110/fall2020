'''
What was the average time of someone completing 
the boston marathon in 2015?
'''

import utilities

file_path = utilities.get_file_path('marathon_results_2015.csv')
f = open(file_path, 'r', encoding='utf8')


print('analyze file here...')


f.close()