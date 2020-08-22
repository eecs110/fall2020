my_list = ['red', 'pink', 'purple', 'orange', 'teal', 'blue']
print(my_list)

# 1. Detecting the length of a list:
print('The length of the list is:', len(my_list))

# 2. Indexing a list:
print('The first item in my list is:', my_list[0])

# 3. Appending an element to a list:
print('adding an item to the end of the list...')
my_list.append('some value')
print('after:', my_list)

# 4. Removing an element from a list (from the bottom):
print('removing last item...')
my_list.pop()
print('removed:', my_list)

print('removing first item...')
my_list.pop(0)
print('removed:', my_list)