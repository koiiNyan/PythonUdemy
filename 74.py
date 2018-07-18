# Question: Please concatenate this file with this one to a single text file.

import pandas as pd

data = pd.read_csv('http://www.pythonhow.com/data/sampledata.txt')
data2 = pd.read_csv('http://www.pythonhow.com/data/sampledata_x_2.txt')
conc_data = pd.concat([data, data2])

conc_data.to_csv('sampledataconcat.txt', index=None)
