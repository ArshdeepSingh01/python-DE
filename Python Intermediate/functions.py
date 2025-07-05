def my_function1(a):
    print("Arshdeep Singh",a)

my_function1("24")

## Arbitrary keyword arguments (kwaargs)
def my_function2(**a):
    print("Arshdeep Singh",a['age'])


my_function2(age= 24)

try:
    my_function2(24)
except Exception as e:
    print(e)
finally:
    print("Printed successfully")

x = lambda a,b:b+2*a
print(x(2,4))

def my_lambda_function(a,b,c):
    return lambda a: a+b+c

a = my_lambda_function(1,2,3)
print(a(4))

# Recursion example 
def my_recursive_func(k):
    if(k>0):
        result = k+my_recursive_func(k-1)
    else:
        result=0
    return result

print(my_recursive_func(4))

