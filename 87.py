# Add the missing items to the file

checklist = ["Portugal", "Germany", "Spain"]
checklist = [country + "\n" for country in checklist]

with open("countries-missing.txt", "r", encoding="utf-8") as file:
    text = file.readlines()
new_text = sorted(checklist + text)


with open("countries-add.txt", "w", encoding="utf-8") as file:
    for row in new_text:
        file.write(row)
