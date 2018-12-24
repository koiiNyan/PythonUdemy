import requests

text = requests.get('http://www.pythonhow.com/data/universe.txt')
print(text.text)
