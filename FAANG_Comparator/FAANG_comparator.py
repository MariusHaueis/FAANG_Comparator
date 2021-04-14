#This is my share price visualisation of the FAANG stocks.
#@author Marius Haueis
#@version 14.04.2021

from matplotlib import pyplot as plt
import pandas_datareader.data as web

api_key = None #insert your Tiingo api key here.
time = [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
money = [0, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000]

#Data import and storage into variables.
facebook = web.get_data_tiingo("FB", api_key=api_key)
google = web.get_data_tiingo("GOOGL", api_key=api_key)
amazon = web.get_data_tiingo("AMZN", api_key=api_key)
aaple = web.get_data_tiingo("AAPL", api_key=api_key)
netflix = web.get_data_tiingo("NFLX", api_key=api_key)

#Creating the curves.
plt.plot(range(len(facebook)), facebook["close"])
plt.plot(range(len(google)), google["close"])
plt.plot(range(len(amazon)), amazon["close"])
plt.plot(range(len(aaple)), aaple["close"])
plt.plot(range(len(netflix)), netflix["close"])

plt.legend(["Facebook", "Alphabet", "Amazon", "Apple","Netflix"], loc = 2)
plt.title("FAANG Share price comparison")
plt.xlabel("Time in years")
plt.ylabel("Prince in Dollar")

ax = plt.subplot()
ax.set_xticklabels(time)
ax.set_yticklabels(money)

plt.show()

