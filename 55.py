# Question: Please add a new employee to the dictionary.

d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"firstName": "Peter", "lastName": "Jones"}],
"owners":[{"firstName": "Jack", "lastName": "Petter"},
          {"firstName": "Jessy", "lastName": "Petter"}]}

emp = d['employees']
empl = {'firstName': 'Kate', 'lastName': 'Green'}
emp.append(empl)
emp.append(dict(firstName = 'Alex', lastName = 'Lee'))
print(d['employees'][3])
print(d['employees'][4])
