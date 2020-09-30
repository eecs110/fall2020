################################################################
# Scope 3: Global variables can be accessed inside of a function
################################################################

name1 = 'Lindsay'

def demo_3(name):
    print(name)
    print(name1)

demo_3('Walter')
