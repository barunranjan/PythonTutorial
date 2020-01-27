from math import sqrt
# Q1 . Write a python script to add two numbers taken from user through keyboard.

x = int(input("enter first number"))
y = int(input("enter second number"))
z = x+y
print(z)


# Q2. Python script to calculate area of circle radius taken from the user.

r = int(input("please enter the radius"))
area = 3.14*r**2
print("area is ", area)


# Q3. python script to calculate Simple interst.

p = int(input("enter principal amount"))
r = int(input("Enter rate of interest"))
t = int(input("enter duration"))
SI = (p*r*t)/100
print("Si is ", SI)


# Q4. calculate square of a given number.

x=int(input("enter a number"))
sqaure = x*x
print(sqaure)


# Q5. Find area of a triangle side taken from the user.

x=int(input("enter first side"))
y=int(input("enter second side"))
z=int(input("enter third side"))
a = (x+y+z)/2
aea = (sqrt(a*(a-x)*(a-y)*(a-z)))
print(aea)
