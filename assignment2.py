# Q1. Write a python script to check if a given number is odd or even

# x = int(input("enter the number"))
# if x%2 == 0:
#     print("{}, is even".format(x))
# else:
#     print("{}, is odd".format(x))


# Q2. Write a python script to check if a number is divisible by 5 or not

# x = int(input("enter the number"))
# if x%5==0:
#     print("{} is divisible by 5".format(x))
# else:
#     print("{} is not divisible by 5".format(x))


# Q3. Find if a number is positive , negative or zero

# x = int(input("enter a number"))
# if x > 0:
#     print("{}, is positive".format(x))
# elif x<0:
#     print("{}, is negative".format(x))
# else:
#     print("{} is zero".format(x))


# Q4. Find greatest among 3 number

# x=int(input("enter first number"))
# y=int(input("enter second number"))
# z=int(input("enter last number"))
# if x>y & x>z:
#     print("{} is greatest".format(x))
# elif y>x & y>z:
#     print("{} is greatest".format(y))
# else:
#     print("{} is greatest".format(z))


# Q5. Python script to check if a year is leap year or not

# x=int(input("enter the year"))
# if x%4==0 and x%100 != 0:
#     print("{}, is a leap year".format(x))
# else:
#     print("{}, is not a leap year".format(x))


# Q6. Python script to take month value in numeric format and check if it has 30 days or 31 days

# x=int(input("enter the month"))
# if x==1 or x==3 or x==5 or x==7 or x==8 or x==10 or x==12:
#     print("{},Month has 31 days".format(x))
# elif x==2:
#     print("{}, has 28/29 days".format(x))
# elif x>12:
#     print("{}, not a valid month".format(x))
# else:
#     print("{}, has 30 days".format(x))


# Q7. Python script to print  word in dicitionary order, word taken from user

# x=input("enter first word")
# y=input("enter second word")
# z=input("enter third word")
# if x > y and x >z  and y > z:
#     print("{}{}{}".format(x,y,z, sep=','))
# elif y>x and y>z and x>z:
#     print("{}{}{}".format(y, x, z, sep=","))
# elif z>x and z>y and y>x:
#     print("{}{}{}".format(z, y, x, sep=","))
# elif z>x and z<y:
#     print("{}{}{}".format(y, z, x, sep=","))
# else:
#     print("{}{}{}".format(x, z, y, sep=","))


# Q8 Write pyhon script to accept two complex number and compare there real part

# x = complex(input("enter first complex number"))
# y = complex(input("enter second complex number"))
# if x.real>y.real:
#     print("{}>{}".format(x,y))
# else:
#     print("{}<{}".format(x,y))


# Q9 Write python script to accept mark of 5 subject from user(assuming maximum marks as 100).
#  Display student pass or fail. If pass also display pass and then also display percentage and division.

# marks=[]
# x=marks.append(int(input("enter 1st Number")))
# y=marks.append(int(input("enter 2nd Number")))
# z=marks.append(int(input("enter 3rd Number")))
# a=marks.append(int(input("enter 4th Number")))
# b=marks.append(int(input("enter last Number")))
# print("marks",marks)
# # status = (x+y+z+a+b)/5
# sum = 0
# for num in marks:
#     sum = sum + num
# print("percentage::", sum )
# status = sum/5
#
# print("status",status)
# if sum < 33 :
#     print("you are fail")
# else:
#     print("You are pass and your percentage is {} %".format(status), "and your
#     division is first class " if status > 90 else "second division")


# Q 10 Python script to check nature of root in quadratic equation.

x= int(input("enter coff of x square"))
y= int(input("enter coff of x"))
c= int(input("enter const"))
print("your equation is {}x2 +{}x +c".format(x,y,c))

d = (y**2) - (4*x*c)
print("d",d)
