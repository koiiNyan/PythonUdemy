# A program that asks the user to submit text repeatedly.
# Saves changes when user submits save
# Closes when the user submits close + save changes.

running = True

while running:
    usr_inp = input('Enter text: ')
    file = open('user_inp_save_close.txt', 'a')
    if usr_inp.lower() == 'close':
        running = False
        file.close()
        break    # If there's no break, 'close' will be stored in a file as well.
    elif usr_inp.lower() == 'save':
        file.close()
        file = open('user_inp_save_close.txt', 'a')
    else:
        file.write(usr_inp + '\n')


# Cant use with open as words will be saved automatically everytime.
