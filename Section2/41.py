# Question: Create a script that generates a text file with all letters of
# English alphabet inside it, one letter per line.
import string

with open('alphabet.txt', 'w', encoding='utf-8') as file:
    alphabet = string.ascii_lowercase
    for letter in alphabet:
        file.write(letter + '\n')
