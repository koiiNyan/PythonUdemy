# Question: Create a script that generates a file where all letters of English
# alphabet are listed three in each line. The inside of the text file would
# look like:
#
# abc
# def
# ghi
#
# and so on.
import string

with open ('3letters.txt', 'w', encoding='utf-8') as file:
    text = string.ascii_lowercase + ' '
    for letter_one, letter_two, letter_three in zip(text[0::3], text[1::3], text[2::3]):
        file.write(letter_one + letter_two + letter_three + '\n')
