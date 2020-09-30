###########################################################
# Scope 4: Global variables can updated with global keyword
###########################################################

name = 'Lindsay'

def modify_name(new_name):
	 global name
	 name = new_name

print(name)
modify_name('Walter')
print(name)
