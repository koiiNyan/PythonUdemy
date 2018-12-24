# Question: Create a script that uses the attached countries_by_area.txt
# file as data source and prints out the top 5 most densely populated countries
#
# Expected output:
#
# India
# Pakistan
# Nigeria
# China
# Indonesia

import pandas as pd
data = pd.read_csv('countries-by-area.txt')
density = data['population_2013'] / data['area_sqkm']
data['density'] = density
sorted_data = data.sort_values(by=['density'], ascending=False)

for country in sorted_data['country'][:5]:
    print(country)
