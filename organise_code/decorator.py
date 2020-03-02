# function decorator doesnot change the function but enahance the function


def decor_result(result_fun):
    def distinction(*marks):
        for m in marks:
            if m>=75:
                print("you got distiction")
                break
        else:
            result_fun(marks)
    return distinction



@decor_result
def result(marks):
    for m in marks:
        if m >= 33:
            pass

        else:
            print("fail")

result([50,45,15,55,18])
