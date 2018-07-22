import sqlite3 as lite
import pandas as pd


con = lite.connect('database.db')

with con:
    cur = con.cursor()
    sql = "SELECT * FROM countries WHERE area > 2000000"
    cur.execute(sql)
    data = cur.fetchall()

df = pd.DataFrame.from_records(data)
df.columns = ['Rank', 'Country', 'Area', 'Population']
df.to_csv('countries-from-db.csv', index=False)
