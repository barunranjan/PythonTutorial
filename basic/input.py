# More on Input instruction


# Reading single value
# x = input("enter the value")
# so if we check the type it will be string by default,
# to change the string into desired data type we have call a function
# print(x, "==> type", type(x))


# Reading a specfic data-type
# x = int(input("enter a number"))
# print(x, "==> type", type(x))


# But suppose if we don't know what the user will enter, then it will through error
# to overcome this problem we have to use "EVAL" function
# x = eval(input("enter a number"))
# print(x, "==> type", type(x))

# eval function will take list dict and many other data type and will evaluate it accordingly

# ================================================================================================================================


# Reading more than 1 value at a time
# x,y = input("enter first number"), input("enter second number")
# print("x==>",x, "y==>",y)

# or
# x,y = input("enter two nuber").split()
# print(x,y)
#
# a,b = input("enter two nuber").split(",")
# print(a,b)

# x = input("enter few words").split()
# print("x::",x, type(x))

# d = input("enter today date").split('/')
# print("type::",d)

d,m,y = input("enter today date").split('/')
print("type::",d,m,y, type(d))