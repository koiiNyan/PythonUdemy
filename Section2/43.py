# Question: Create a script that generates a file where all letters of
# English alphabet are listed two in each line. The inside of the text file
# would look like:
#
# ab
# cd
# ef
#
# and so on.
import string

with open ('2letters.txt', 'w', encoding='utf-8') as file:
    text = string.ascii_lowercase
    for letter_one, letter_two in zip(text[0::2], text[1::2]):
        file.write(letter_one + letter_two + '\n')
