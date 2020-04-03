# x = int(input("enter first number"))
# y = int(input("enter second number"))
# try:
#     z=x/y
#     print("division-result is", z)
# except ZeroDivisionError:
#     print("invalid denominator")
# finally:
#     print("final code")

# Rule for try-except block
# 1) Inside the try block only those code are written in which we can get exception.
# 2) No except block without try block
# 3) Except block should match the actual exception
# 4) No exception will be raise if try block has been executed.
# 5) Many except block can be written inside a try block
# 6) finally block always run
# 7) We can use else also with try except block, but it will run only when no exception raised.
# 8) finally will run in all cases even when exception comes or not but else will run only when no exception raised


# x = int(input("enter first number"))
# y = int(input("enter second number"))
# try:
#     if y==0:
#         raise ZeroDivisionError("Denominator can not be zero")
#     z = x/y
#     print("result is", z)
# except ZeroDivisionError:
#     print("zero division")


class InsufficientBalance(ZeroDivisionError):
    def __init__(self, arg):
        self.msg = arg
balance = 5000
w = int(input("enter amount"))
try:
    if w>balance:
        raise InsufficientBalance("Insufficient Balance in the account")

    balance = balance-w
    print("Your Transction was successful")
except InsufficientBalance as i:
    print(i.msg)
else:
    print("withdraw amount", w, "Successfully")
finally:
    print("Available Balance is", balance)