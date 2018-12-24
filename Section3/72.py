# Create a script that let the user type in a search term and open and search
# on the browser for that term on Google

import webbrowser


def google_search(query):
    search = webbrowser.open('https://www.google.ru/search?q={}'.format(query))
    return search


query = input("Enter your query: ")
google_search(query)
