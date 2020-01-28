"""List of operator in python are
1. Arithmetic Operator
2.relational Operator
3. Logical Operator
4. Bitwise Operator
5. Assignment Operator
6. Identity Operator
7. Membership Operator"""

# from operator import itemgetter

# Arithmetic operator

'''Exponent operator used for exponent and it work for negative exponent also'''
a = 3**2
print("exponent of a =", a)

b = 2**-3
print("exponent of b =", b)

c = -2**3
print("exponent of b =", c)


# Divide Operator

# In single divide whether the operant are float or int the result is float

z = 5/3
print("/ it will give float value of Z =", z)

x = 6/3
print("/ it will give float value of Z =", x)


'''In Double divide it the operant are float  result is float and if 
operant are int the result is int and value is floor value'''

s = 5//3
print("// it will give float value of S =", s)

t = 6//3
print("// it will give float value of T =", t)

r = 5.0//3.0
print("// it will give float value of S =", r)

p = 6//3.0
print("// it will give float value of T =", p)

# Modulas operator(remainder)

l = 8%3
print("remainder here is for l is",l)

m = 8%10
print("remainder here is for m is",m)

s= 4.3%3
print("remainder of float is always float s =",s)

k= -4%3
print("remainder of such cases depend upon denominator sign which is positive here k =",k)

negative_k= 4%-3
print("remainder of such cases depend upon denominator sign which is positive here -k =",negative_k)


'''relational operator'''
"""All non-zero value are consider as True and zero value is consider as False"""
x = True
y = int(x)
print(y)

a = False
b = int(a)
print(b)

x = 4
y = bool(x)
print(y)

'''In complex number only equality operator will work greater than(<,<=) 
   and less than(>, >=) to will not work for the complex number '''

s = True+5
# Addition will work with the boolean value
print(s)


'''those operants which take two value for its function is called is BINARY OPERATOR'''

s = 5 and 4
'''if x and y are non-boolean then result is also non-boolean but 
    IF X IS FALSE THE RESULT IS X OR OTHERWISE RESULT IS Y'''
print(s)

'''IMPORTANT
# not True --> false
# not False --> True
# Empty String = "" --> False
# non-empty string --> true'''

# Assignment operator
x1 = 5
x1*= 3 + 4
x2 = 5
x2= x2*3+5
print(x2)
print(x1)
