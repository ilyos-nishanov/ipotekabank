#%%
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#%% open file
with open('usd_rate_time_series_fluctuated.json') as f:
    data = json.load(f)

#%% get dates
dates = list(data['rates'].keys())
dates

#%% get rates
rates = {currency: [] for currency in data['rates'][dates[0]].keys()}

for date in dates:
    for currency, rate in data['rates'][date].items():
        rates[currency].append(rate)
rates

#%% calculate volatility
volatility = {}
for currency, rate_list in rates.items():
    returns = np.diff(rate_list) / rate_list[:-1]  # Calculate returns
    volatility[currency] = np.std(returns)  # Calculate standard deviation

#let's save this
volatility_df = pd.DataFrame(list(volatility.items()), columns=['Currency', 'Volatility'])
volatility_df.to_excel('currency_volatilities.xlsx', index=False)

#%% top 3 volotile rates
top_volatility = sorted(volatility.items(), key=lambda x: x[1], reverse=True)[:3]
top_currencies = [item[0] for item in top_volatility]
top_volatility_values = [item[1] for item in top_volatility]

#%% plotting
plt.figure(figsize=(10, 5))
for currency in top_currencies:
    plt.plot(dates, rates[currency], label=currency)

plt.title('Top 3 Most Volatile Currency Rates')
plt.xlabel('Date')
plt.ylabel('Exchange Rate (to USD)')
plt.xticks(dates[::5], rotation=45)  # Rotate x-axis labels for better readability
plt.legend()
plt.tight_layout()

#%% save as jpeg
plt.savefig('top_3_most_volatile_rates.jpeg', format='jpeg')
plt.show()
# %%
