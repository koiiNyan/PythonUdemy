# Question: Create a program that once executed the program prints Hello
# instantly first, then it prints it after 1 second, then after 2, 3, 4,
# and so on the interval increases between prints.

from time import sleep
counter = 0
while True:
    counter += 1
    print("Hello")
    sleep(counter)
