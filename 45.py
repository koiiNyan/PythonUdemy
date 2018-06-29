# Question: Please create a script that generates 26 text files named a.txt,
# b.txt, and so on up to z.txt. Each file should contain a letter reflecting
# its filename. So, a.txt will contain letter a,
# b.txt will contain letter b and so on.

import string
alphabet = string.ascii_lowercase
for char in alphabet:
    with open("{}.txt".format(char), "w", encoding="utf-8") as file:
        file.write(char)
