# Question:  Why is there an error in the code and how would you fix it?
#
# def foo(a=1, b=2):
#    return a + b
#
# x = foo - 1
#
# There's an error because we don't call for function. (With brackets)

def foo(a=1, b=2):
    return a + b

x = foo () - 1
print(x)
