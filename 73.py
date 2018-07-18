# Multiply the values of the text file in the URL by two and export the output
# to a new file

import pandas as pd

data = pd.read_csv('http://www.pythonhow.com/data/sampledata.txt')
data *= 2
data.to_csv('sampledata.txt', index=None)
