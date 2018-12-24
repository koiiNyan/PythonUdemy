# Question: The code produces an error. Please understand the error and try to
# fix it

age = input("What's your age? ")
age_last_year = int(age) - 1
print("Last year you were %s." % age_last_year)

# Input is a str, so to do the maths we need to convert string to int.
