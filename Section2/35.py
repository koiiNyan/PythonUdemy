# Question: Create a function that takes any string as input and returns
# the number of words for that string.

def words_len(stringg):
    st = stringg.split()
    length = len(st)
    return length

stringg = input("Number of words in this string: ")

print("is {}".format(words_len(stringg)))
