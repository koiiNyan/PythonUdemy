with open("countries-raw.txt", "r", encoding="utf-8") as file:
    text = file.readlines()

text = [row.strip("\n") for row in text if "\n" in row]
text = [row for row in text if row != ""]
text = [row for row in text if len(row) != 1]
text = [row for row in text if row != "Top of Page"]
print(text)

with open("countries.txt", "w", encoding="utf-8") as file:
    for row in text:
        file.write(row + "\n")
