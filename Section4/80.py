# Create a script that lets the user submit a password until they have satisfied
# three conditions:
# 1. Password contains at least one number
# 2. Contains one uppercase letter
# 3. It is at least 5 chars
# Give the exact reason why the user has not created a correct password
import string

correct_pass = False
while correct_pass == False:
    password = input("Enter new password: ")
    if any(char.isdigit() for char in password) and any(char.isupper() for char in password)\
    and len(password) >= 5:
        print("Password is fine")
        correct_pass == True
        break
    if not any(char.isdigit() for char in password):
        print("Password should contain at least one number")
    if not any(char.isupper() for char in password):
        print("Password should contain at least one uppercase letter")
    if len(password) < 5:
        print("Password should be at least 5 characters long")
