import requests

response = requests.get('http://www.pythonhow.com/data/universe.txt')
response_text = response.text
a_count = response_text.count('a')
print(a_count)
