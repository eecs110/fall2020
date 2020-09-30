##############################################################
# Scope 2: Local variables take precedence over global 
#          variables
##############################################################

name = 'Lindsay'

def demo_2(name):
    print(name)  # note: prints the name "Walter" (and not "Lindsay")

demo_2('Walter')
