# Q1 Python script to check if a number is prime or not.

# x=int(input("enter the number"))
# for i in range(2,x):
#     if x%i==0:
#         print("{} not a prime".format(x))
#         print("{} times {} is {}".format(x/i,i,x))
#         break
# else:
#     print("{} is prime".format(x))


# Q2 Python script to print next prime number of given number

# x=int(input("enter the number"))
# while True:
#     x = x + 1
#     for i in range(2,x):
#         if x%i==0:
#             x = x + 1
#             break
#
#     else:
#         print(x)
#         break

# Q3 Python script to print first N prime number. value of N taken from user.

# x=int(input("enter the range"))
# for i in range(2, x + 1):
#     for n in range(2, i):
#         if (i % n) == 0:
#             break
#     else:
#         print(i)


# Q4 Python script to print prime number between two numberr.

# low=int(input("enter the lower limit"))
# up= int(input("enter the upper limit"))
# for i in range (low, up+1):
#     for n in range(2,i):
#         if i%n == 0:
#             break
#     else:
#         print(i)

# Q5 Python script two check if two number are co-prime or not

# x=int(input("enter 1st number"))
# y=int(input("enter 2nd number"))
# if x>y:
#     smaller= y
# else:
#     smaller= x
# for i in range(1, smaller+1):
#     if (x%i==0) and (y%i==0):
#         hcf=i
#
# if hcf == 1:
#     print("It is co-prime number")
# else:
#     print("not a co-prime number and hcf is {}".format(hcf))


# Q6 Python script to print first N odd natural number in reverse order using range function in loop.
x=int(input("enter the value"))
for i in range(x+1,0,-1):
    if i%2!=0:
       print("even",i)




