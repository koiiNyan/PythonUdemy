# A program that asks the user to input values seperated by commas and those
# values will be stored in a seperate line each in a text file

usr_inp = input('Enter values, seperated by commas: ')

seperator = usr_inp.split(',')

with open('text_from_usr.txt', 'a') as file:
    for i in seperator:
        file.write(i + '\n')
