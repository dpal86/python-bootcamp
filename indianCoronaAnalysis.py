import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
import opendatasets as od
# import cgi

# pip install opendatasets
data = od.download("https://www.kaggle.com/datasets/imdevskp/corona-virus-report")

df = pd.read_csv("corona_data/covid_19_clean_complete.csv")
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

print(df.dtypes)

df['Date'] = pd.to_datetime(df['Date'])
print(df['Date'].head())
print(df['Date'].dtype)
print(df.head())

unique_countries=df['Country/Region'].unique()
print("Unique Countries" , unique_countries)

groupBy_Date = df.groupby(df["Date"]).sum()

print("Group By Date :",groupBy_Date)

global_confirmed = df.groupby('Date')['Confirmed'].sum()

print("Confirmed death groupby Date :",global_confirmed.head())


plt.figure(figsize=(12,6))
plt.plot(global_confirmed.index, global_confirmed.values, color='blue', marker='o', linestyle='-')
plt.title("Global Confirmed COVID-19 Cases Over Time")
plt.xlabel("Date")
plt.ylabel("Total Confirmed Cases")
plt.grid(True)
#plt.show()


latest_date = df['Date'].max()
print("Latest date in dataset:", latest_date)

latest_data = df[df['Date'] == latest_date]

print(latest_data.head())

top_10_Countries = df.groupby('Country/Region')['Confirmed'].sum().sort_values(ascending=False).head(10)

print("Top 10 countries",top_10_Countries)

plt.figure(figsize=(12,6))
top_10_Countries.plot(kind='bar', color='skyblue')
plt.title("Top 10 Countries with Highest Confirmed COVID-19 Cases")
plt.xlabel("Country")
plt.ylabel("Confirmed Cases")
plt.xticks(rotation=60)
plt.grid(axis='y')
#plt.show()

pivot_table = pd.pivot_table(
    df,
    index='Country/Region',
    columns='Date',
    values='Confirmed',
    aggfunc='sum'   
)

print(pivot_table.head(10))

plt.figure(figsize=(16,10))
sns.heatmap(pivot_table, cmap="YlGnBu", cbar=True)

plt.title("Heatmap of Confirmed COVID-19 Cases by Country and Date")
plt.xlabel("Date")
plt.ylabel("Country/Region")
plt.show()