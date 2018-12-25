# A program that asks the user to submit text repeatedly.
# Closes when the user submits close.

running = True

while running:
    usr_inp = input('Enter text: ')
    if usr_inp.lower() == 'close':
        running = False
        break    # If there's no break, 'close' will be stored in a file as well.
    with open('user_inp.txt', 'a') as file:
        file.write(usr_inp + '\n')
