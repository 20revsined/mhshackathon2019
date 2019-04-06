import pandas as pd
import matplotlib.pyplt as plt

df = pd.read_csv('dija.csv')
df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date')

stks = ['NKE', 'IBM', 'JPM', 'AAPL', 'GE']

start = '2010'
end = '2016'

rtndf = df[stks][[start:end].pct_change().dropna()


pltdf = df[start:end]

pltflag = True

if pltflag:
  #pandas fig 1
  pltdf[stks].pct_change().plot()
  
  #pandas fig 2
  pltdf[stks].pct_change().dropna.cumsum().plot()

  stkind = 0

  ## Matplotlib plots
  plt.figure()
  plt.plot()

  for stkind in range(len(stks)):
    plt.subplot(2, 2, stkind + 1)
    plt.plot(tmpdf.index,tmpdf.values)
    tmpdf = pltdf[stks[stkind]]
    plt.title('Prices of ' + stks[stkind] + ' from ' + start + ' to ' + end)
    plt.xlabel('Dates')
    plt.ylabel('Price')
  plt.show()
