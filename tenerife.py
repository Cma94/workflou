import pandas as pd
import requests
import matplotlib.pyplot as plt

df=pd.read_csv('turZo.csv', parse_dates=True, sep=',', encoding = "ISO-8859-1")

plt.plot(df.año,df.total)

plt.savefig('tenerife.png')