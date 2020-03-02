# when we are not sure of how many argument would be given by the user we use variable length argument
# def fun(*n):
#     print(n, type(n))
# fun(10,20,30,40,50)

# program to find average

# def avg(*n):
#     x=0
#     for i in n:
#         x = x+i
#     if len(n)!=0:
#         return x/len(n)
#     else:
#         return "no element"
#
# average = avg()
# print("average is ", average)

# def class1(name, *marks):
#     print(name, end="")
#     s=0
#     for i in marks:
#         s=s+i
#     per=s/len(marks)
#     print(" total marks is", per,"%")
#
# class1("ajay",20,30,40,50,60)

# If while defining function having keyword argument, we first pass the variable length keyword argument then while calling
# the function we need to pass keyword argument.

# def class1(*marks, name):
#     print(name, end="")
#     s=0
#     for i in marks:
#         s=s+i
#     per=s/len(marks)
#     print(" total marks is", per,"%")
#
# class1(20,30,40,100,60, name="Rahul")

# ========================================================================================================================================


# Variable length keyword argument

# If we call a function and then we pass the argument as key value pair, then we need Variable length keyword argument

# def fun(**kwargs):
#     print("Person detail")
#     for key, value in kwargs.items():
#         print(key, "-", value)
# fun(NAME = "Varun Ranjan", Empid= 70, Salery=15517)

# == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==

# s=(lambda a,b: a if a>b else b)(20,25)
# print(s)

# s=(lambda a,b: a if a>b else b)(int(input("enter 1st number")), int(input("enter 2nd number")))
# print("Greater is ", s)

# ====================================================================================================================================


# Lambda with recursion

s= lambda a : 1 if a==0 else a*s(a-1)
x=s(5)
print(x)