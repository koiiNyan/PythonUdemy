# Adding countries to db

import sqlite3
import pandas as pd

df = pd.read_csv('ten-more-countries.txt')
con = sqlite3.connect('database.db')


df.to_sql("countries", con, if_exists='append',index=False)

# Checking
cur = con.cursor()
sql = "SELECT * FROM countries"
cur.execute(sql)
results = cur.fetchall()
print(results)

con.commit()
con.close()
