# Question: Create a script that asks the user to enter their age and the script
# calculates the user's year of birth and prints it out in a string like in the
# expected output. Please make sure you generate the current year dynamically.
#
# Expected output:
#
# We think you were born back in 1988

from datetime import date
current_date = date.today()
current_year = current_date.year
user_age = input('Please enter your age: ')
user_birthyear = current_year - (int(user_age))
print('We think you were born back in {}'.format(user_birthyear))
