# lower()
# returns a copy of the string that is all lowercase
result = 'My string'.lower()			
print(result)

# upper()
# returns a copy of the string that is all uppercase
result = 'My string'.upper()			
print(result)

# replace()
# returns a copy of the string where any instances of the first argument are replaced by the second argument
result = 'My string'.replace(' ', '_')	
print(result)

# find()    
# returns the position where the first instance of the argument is found. Returns -1 if argument not found
result = 'My string'.find('s')			
print(result) 
result = 'My string'.find('!')			
print(result) 

# format()   
# allows you to format and inject data into a string
# format() with a positional argument:
result = 'Hello {0}'.format('Walter')	
print(result) 

# format() with a keyword argument:
result = 'Hello {name}'.format(name='Tanu')	
print(result) 	
