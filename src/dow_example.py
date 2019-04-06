import pandas as pd
import matplotlib.pyplt as plt

df = pd.read_csv('dija.csv')
df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date')

stks = ['NKE', 'IBM', 'JPM', 'AAPL', 'GE']

start = '2010'
end = '2016'

pltdf = df[start:end]

stkind = 0
tmpdf = pltdf[stks[stkind]]
plt.figure()
plt.plot()

for stkind in range(len(stks)):
  plt.plot(tmpdf.index,tmpdf.values)

plt.title('Prices of ' + stks[stkind] + ' from ' + start + ' to ' + end)
plt.xlabel('Dates')
plt.ybael('Price')
plt.show()
