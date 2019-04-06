import pandas as pd
import matplotlib.pyplt as plt

df = pd.read_csv('dija.csv')
df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date')

stks = ['NKE', 'IBM', 'JPM', 'AAPL', 'GE']

start = '2010'
end = '2016'

pltdf = df[start:end]

plt.figure()
plt.plot()

tmpdf = pltdf[stks[0]]
plt.plot(tmpdf.index,tmpdf.values)
plt.show()
