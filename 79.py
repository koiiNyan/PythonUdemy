# Create a script that lets the user submit a password until they have satisfied
# three conditions:
# 1. Password contains at least one number
# 2. Contains one uppercase letter
# 3. It is at least 5 chars
# Print out msg "Password is not fine" if user didn't create a correct password
import string

correct_pass = False
while correct_pass == False:
    password = input("Enter new password: ")
    if any(char.isdigit() for char in password) and any(char.isupper() for char in password)\
    and len(password) >= 5:
        print("Password is fine")
        correct_pass == True
        break
    else:
        print("Password is not fine")
