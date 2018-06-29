# Write a script that iterates through each of the 26 text files, checks if the
# letter inside the text file is in string "python" and puts the letter in a
# list if the letter is a character of "python"
import glob
file_list = glob.glob("*.txt")
python_list = []
for filename in file_list:
    with open(filename, 'r') as file:
        text = file.read()
        if text in "python":
            python_list.append(text)

print(python_list)
