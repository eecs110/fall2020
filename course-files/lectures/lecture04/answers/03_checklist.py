# Write a program that dynamically creates a "TODO" list on-the-fly.
# You will ask the user what they need to do, and store it in a list.
# Do this 5 times, and at the end of the program, print out the list

my_list = []
print('This program will allow you to create a TODO list.')


task = input('\nWhat do you have to do today? ')
my_list.append(task)

task = input('\nWhat do you have to do today? ')
my_list.append(task)

task = input('\nWhat do you have to do today? ')
my_list.append(task)

task = input('\nWhat do you have to do today? ')
my_list.append(task)

task = input('\nWhat do you have to do today? ')
my_list.append(task)


print('\nThere are', len(my_list), 'items in your TODO list:')
print(my_list)