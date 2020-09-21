# Write a program that dynamically creates a "TODO" list on-the-fly.
# You will ask the user what they need to do, and store it in a list.
# Do this 5 times, and at the end of the program, print out the list


my_list = []
print('This program will allow you to create a TODO list.')

# Preview of a while loop:
# you will learn more about the while loop in a few weeks. For now, all you need
# to know is that it repeats the statements inside of the "while block" until the 
# while condition (len(chores) < 5) is False:

while len(my_list) < 5:
    # these statements will execute until the length of the list is 5 or more.
    task = input('\nWhat do you have to do today? ')
    my_list.append(task)


print('\nThere are', len(my_list), 'items in your TODO list:')
print(my_list)