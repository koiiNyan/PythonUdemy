# Write a script that extracts letters from the 26 text files and put the
# letters in a list
import string
letters = string.ascii_lowercase
letters_list = []

for filename in letters:
    with open("{}.txt".format(filename), "r", encoding="utf-8") as file:
        text = file.read()
        letters_list += text

print(letters_list)
