# Question: Create a program that once executed the programs prints Hello
# instantly first, then it prints it after 1 second, then after 2, 3, and then
# the program prints out the message "End of the Loop" and stops.

from time import sleep
counter = 0
while True:
    counter += 1
    print("Hello")
    if counter > 3:
        print("End of the Loop")
        break
    sleep(counter)
