# Question: Please take a look at the following list:
#
checklist = ["Portugal", "Germany", "Munster", "Spain"]
#
# One of the items is not a country. Please use Python and the file containing
# the list of countries (attached) as data source to filter out the checklist
# of non-country items. Once you have filtered out checklist, then print it out
#
# Expected output:
#
# ['Germany', 'Portugal', 'Spain']
#
with open("countries.txt", "r", encoding="utf-8") as file:
    text = file.readlines()
text = [row.strip("\n") for row in text]
sorted_list = [country for country in checklist if country in text]
print(sorted_list)
