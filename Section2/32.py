#Question:  What will the following script output? Please try to do this mentally if you can.
#
c = 1
def foo():
    return c
c = 3
print(foo())

# Output will be 3 as function is called after 3 assigned to c.
