# ## Example 1: 
# Note that while lists are surrounded by square brackets, tuples are
# surrounded by parenthesis
tuple_of_strings = ('freshman', 'sophomore', 'junior', 'senior')

# parenthesis optional, but recommended
tuple_alternate_method_to_initialize = 'freshman', 'sophmore', 'junior', 'senior'

tuple_of_ints = (12, 24, 36, 48, 60)
tuple_of_booleans = (True, True, False)
tuple_of_tuples = ((20, 20), (20, 40), (40, 40), (40, 20))
tuple_of_mixed_data_types = ('a', 123, (40, 40), False)

print('\n\ntuples of different types...')
print(type(tuple_of_strings))
print(tuple_of_strings)
print(tuple_alternate_method_to_initialize)
print(tuple_of_ints)
print(tuple_of_booleans)
print(tuple_of_tuples)
print(tuple_of_mixed_data_types)
# ## End Example 1



# ## Example 2: You can't edit add to, remove from, or update data in a tuple
# uncomment to see the errors
# print('\n\nYou can't edit add to, remove from, or update data in a tuple...')
# print(tuple_of_strings)  
# tuple_of_strings.pop()  # results in an error
# tuple_of_strings.append('masters')  # results in an  error
# tuple_of_strings[0] = 'freshling'  # results in an error
# print(list_of_strings)
# # ## End Example 2