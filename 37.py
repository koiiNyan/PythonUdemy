# Question: Create a function that takes a text file as input and returns
# the number of words contained in the text file. Please take into consideration
# that some words can be separated by a comma with no space.
# For example "Hi,it's me." would need to be counted as three words. For your
# convenience, you can use the text file in the attachment.

def word_count(file):
    with open(file, "r", encoding="utf-8") as file:
        text = file.read()
        text = text.replace(',', ' ')
        text = text.split()
        return len(text)


print(word_count("words2.txt"))
