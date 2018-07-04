# Question: Please download the file in the attachment and use Python to print out
# its content.

import json
from pprint import pprint

with open('company1.json', 'r') as file:
    file_for_printing = json.load(file)
    pprint(file_for_printing)
