class JustNotCoolError(Exception):
    pass
x = 2
try:
    raise JustNotCoolError("This is not cool")
    #raise Exception("This is an exception")
    #print(x / 1)
    #if not type(x) is str:
    #    raise TypeError("x is not a string")
except NameError:
    print("NameError: x is not defined")
except ZeroDivisionError:
    print("ZeroDivisionError: division by zero")
except Exception as error:
    print("Exception: ", error)
else:
    print("No exceptions")
finally:
    print("Finally block")