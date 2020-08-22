########################################################
# Scope 5: Without global keyword, Python assumes you’re 
#          creating a new local variable
########################################################

name = 'Lindsay'

def modify_name(new_name):
	 name = new_name

print(name)
modify_name('Walter')
print(name)

