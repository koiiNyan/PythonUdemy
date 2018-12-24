# Question: Please download the json file in the attachment and use Python to
# add a new employee to the content of the file so that the file looks like in
# the expected output below.

import json
from pprint import pprint

with open('company1.json', 'r') as file:
    file_for_printing = json.load(file)
    file_for_printing['employees'].append(dict(firstName = 'Albert',\
    lastName = 'Bert'))
    file.seek(0)

with open('company1.json', 'w') as file:
    json.dump(file_for_printing, file, indent=4)

# r+ open for reading and writing
# truncate() erases file content => 0b
