# Q1. Sort a list given by user.

# l = []
# n = int(input("Please enter how much number you want"))
# for i in range(0,n):
#     _list = int(input("enter the value"))
#     l.append(_list)
# print(l)
# # l.sort()
# # print(l)
# new_list = []
#
# while l:
#     print("lll",l)
#     minimum = l[0]  # arbitrary number in list
#     print("mmm",minimum)
#     for x in l:
#         if x < minimum:
#             minimum = x
#             print("min",x)
#     new_list.append(minimum)
#     print("nnn",new_list)
#     l.remove(minimum)
#
# print(new_list)


# Q2 Write python script to find greatest number in list given by user.

# l=[]
# n=int(input("how much number you want"))
# for i in range(0,n):
#     li= int(input("enter the value"))
#     l.append(li)
# y=max(l)
# print(y)

# Q3 Find the sum of all the integer the list given by user.

# l=[]
# n=int(input("how many element you want"))
# sum=0
# for i in range(0,n):
#     val=(int(input("enter the value")))
#     l.append(val)
# for i in l:
#     sum=sum+i
# print(sum)
#                          or
# l=[]
# n=int(input("how many prime number you want"))
# for i in range(0,n):
#     val = (int(input("enter the value")))
#     l.append(val)
# print(l)
# sum=0
# for i in range(0,len(l)):
#     sum=sum+l[i]
# print(sum)

# Q4 List of first n prime number, value of n taken from user.
l=[]
n = int(input("how many prime number you want"))
i = 2
if i == 2:
    print(str(i) + "is a prime no")
    i = i+1
c=1
print(i)
while c<n:
    for j in range(2, i):
        if i%j==0:
            break

    if i == j+1:
        l.append(i)
        # print(str(i) + "is aa prime no")
        c=c+1

    i=i+1
    l[0] = 2
print(l)




