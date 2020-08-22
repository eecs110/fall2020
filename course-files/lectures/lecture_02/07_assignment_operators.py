########################
# Assignment Operators #
########################
# Assignment operators are a way of saying: 
# "put the results of the expression stored in the right operand 
# into the left operand." Unlike the three kinds of operators 
# described above, assignment operators are meant to be used with 
# variables.


# Examples of numbers, strings, and booleans

# initialize variables for demo:
a = 20
b = 10
c = 25
c = a + b  # assigns the value of a + b into c
print(c)
c = c + a  # assigns the current value stored in 'c' and the value stored in 'a' to 'c' (c gets replaced)
print(c)
c += a  #  equivalent to c = c + a
print(c)
c -= a  # equivalent to c = c - a
print(c)
c *= a  # equivalent to c = c * a
print(c)
c /= a  # equivalent to c = c / a
print(c)

bool1 = True
bool2 = False
str1 = 'hello '
bool1 = True
int1 = 123
# str1 += bool1     # throws an error if you don't convert it to a string first
# str1 += int1      # ditto: throws an error if you don't convert it to a string first
str1 += str(bool1)
str1 += str(int1)
print(str1)
