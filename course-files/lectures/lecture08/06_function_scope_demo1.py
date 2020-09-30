##############################################################
# Scope 1: Local variables cannot be accessed outside function
# Takeaway: If you want access to a value after the function
#           terminates, you have to return it.
##############################################################

def demo_1(name):
     greeting = 'Welcome, ' + name

demo_1('Jimmy')
# un-comment the line below to see the error:
# print(greeting)  # the variable greeting is undefined outside of the demo_1 function


