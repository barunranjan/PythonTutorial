# l=[] empty list
# ex

# l=[]
# l.append(10)
# l.append(20)
# l.append(30)
# print(l)
# print(l[2])

# itteration in list

# for i in l:
#     print(i)

# Notes:
# List is like as array in c, C++ etc.
# If we cross the uper index of a list it will through an error as list index out of range.


# adding data to list


# Append

# a=[]
# a.append(100)
# a.append(200)
# a.append("ram")
# a.append(105.57)
# print(a)

# Append add data at the end of the list.


# Insert
# With insert function we first add pass the index where we have to
# insert data and then the value which we have to insert.

# x.insert(index, value)

#
# b=[]
# b.insert(0,10)
# b.insert(1,20)
# b.insert(2,30)
# print(b)

# the old value will shift to the right

# b.insert(1,50)
# print(b)
# b[0]=100
# print(b)

# Negative value with insert

# If we insert value at negative index then it is calculated from the end

# b.insert(-1,1000)
# print(b)


# Concatnate two list
# a=[1,10,100]
# b=[2,20,200]
# c=a+b
# print(c)

# In this value get added but not appended in original list.
# a+[1000]
# print(a)

# To append value in original list you need to use compound assignment operator
# b=b+[2000]
# print(b)
#
# c*=3
# print(c)


# Editing list in python


# changing value of list

myList=[10,20,30,40,50]
# print(myList)
# myList[1]=200
# print(myList)


# Removing element from list

myList.remove(40)
print(myList)
myList=myList*3
print(myList)

# If the element has lots of same value, then it will remove the first value.
myList.remove(20)
print(myList)

# sort the list
myList.sort()
print(myList)

# clear the list
# myList.clear()
# print(myList)

# Reverse the list
myList.reverse()
print(myList)

# remove the last element from the list
# In pop we can pass index
myList.pop()
print(myList)


# Other important index function
# myList.index(self,object start, end)
count=myList.count(10)
print("count::",count)