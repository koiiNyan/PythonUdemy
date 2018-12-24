# Question: Please download the words1.txt file from the attachment and then
# create a Python function that takes a text file as input and returns
# the number of words contained in the text file.
#
# Expected output:
#
# 10


def word_count(file):
    with open(file, "r", encoding="utf-8") as file:
        text = file.read()
        text = text.split()
        return len(text)


print(word_count("words1.txt"))
