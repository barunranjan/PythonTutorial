# The argument which we provide during function defination is called formal argument
# while the argument which we give during function call is called actual argument.
# This actual argument goes according to there postion in formal argument,

# But when we specify the postion specifically, it is known as keyword argument

def fun(a, b):
    print("a =",a, "b =",b)
fun(10,20)
fun(a=10, b=20)
# specifying argument accordingly
fun(b=20,a=10)
# If the first argument is keyword argument then all the argument after that should be keyword arrgument

