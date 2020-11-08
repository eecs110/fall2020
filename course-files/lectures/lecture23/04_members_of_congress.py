# How many representatives does each state have in the House?
import sys
import os
from csv import reader
dir_path = os.path.dirname(sys.argv[0])
file_path = os.path.join(dir_path, 'legislators-current.csv')
# End VS Code Hack:

f = open(file_path, 'r', encoding='utf8', errors='ignore')
for row in reader(f):
    print(row)