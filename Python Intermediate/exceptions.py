n=12
try:
    res=100/n
except ZeroDivisionError:
    print("Please update n to a non-zero value")
else:
    print("result is",round(res))
finally:
    print("Operation successful")