import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('http://www.pythonhow.com/data/sampledata.txt')
data.plot(x='x', y='y', kind="scatter", color="violet")
plt.show()
