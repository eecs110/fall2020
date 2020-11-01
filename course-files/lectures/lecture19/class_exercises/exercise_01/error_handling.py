'''
You're working for the city and want to identify all of the senior
citizens in your district to send out a mailer -- as they may qualify
for a special tax waiver. You are given a (messy and incomplete) data
set. Your boss wants you to create 2 files:

  * One for people with a complete data profile (no obvious mistakes)
  * One for people with an incomplete / suspect data profile

Write a program to do this.
'''

import utilities
f = open(utilities.get_file_path('people.csv'), 'r')
for line in f.readlines():
    print(line)