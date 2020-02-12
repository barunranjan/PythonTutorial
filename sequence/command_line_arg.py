# When we run a Python code from the command line.
# It is called command line and if we pass the argument
# from the command line then it is called command line arrgument

from sys import argv

# for x in argv:
#     print(x)

# Every element in argv goes as a string and it become a list.
y=0
s=0
for x in argv:
    if y==0:
        y=1
    else:
        s=s+int(x)
print(s)