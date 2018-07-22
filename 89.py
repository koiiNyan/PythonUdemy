import sqlite3 as lite


con = lite.connect('database.db')

with con:
    cur = con.cursor()
    sql = "SELECT country FROM countries WHERE area > 2000000"
    cur.execute(sql)
    data = cur.fetchall()
    countries_list = []
    for country in data:
        countries_list.append(country[0])

    for country in countries_list:
        print(country)
