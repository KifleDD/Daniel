Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
================== RESTART: C:/Users/DANIEL/Desktop/tryme.4.py =================
>>> # To find the length of triangle if we already know the length of two arguments
# The math format of calculating the third length is as below. 
''' hypotenuse = sqrt (a ** 2 + b ** 2) '''

#Think of what is the ouput if we enter two parameters
# In hypotenuse, the input are two lengths, so we can put two arguments.
# set variable c as return value

def hypotenuse(a, b):
    return 0

# Do a small test now. No matter what we put for arguments, the return value is always 0

# choose a case we know the rught answer. For exmple, if the horizontal is 3 and vertical length is 4, the third length
# of this triangle should be 5.
# we do test to make sure the output is what we want

def hypotenuse(a ,b):
    print('the first length is', a)
    print('the second lengthe is', b)
    return 0


# next step, we need the sum of squares of a and b
# the right output should be 25

def hypotenuse(a ,b):
    dsquared = a**2 + b**2
    print('dsquared is' , dsquared)
    return 0

# Import math method if we want to use built-in function to calculate the ssquare result

import math

def hypotenuse(a ,b):
    dsquared = a**2 + b**2
    result = math.sqrt(dsquared)
    return result
' hypotenuse = sqrt (a ** 2 + b ** 2) '
>>> 