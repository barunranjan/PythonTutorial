
# def add(a,b):
#     x=a+b
#     print(x)
# add(25,25,25)
# def sum(x,y):
#     z = x + y
#     print(z)
# sum(25 ,24+23)

# sum(23+23+21) <= this will give error.
# Default arrgument is a case where we give a fixed value to the argument, if during the function call a none value is provided
# the it consider the default value. EX---
def sum(a=0,b=0,c=0):
    s=a+b+c
    print(s)
sum()
sum(25)
sum(25,24)
sum(25,24,36)

# NOTE : After default argument non default argument are not allowed