# Create a program that generates a password of 6 random alphanumeric characters
import string
import random

letters = string.ascii_letters
digits = string.digits
extra_chars = '!@#$%^&*()?'
characters = letters + digits + extra_chars
password_list = random.sample(characters, 6)
password = "".join(password_list)
print(password)
