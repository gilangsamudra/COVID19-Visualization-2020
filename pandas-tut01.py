import pandas as pd
import matplotlib.pyplot as plt


# Bagian 1 -- Load data dari sumbernya
df = pd.read_csv(
    'https://raw.githubusercontent.com/datasets/covid-19/\
master/data/countries-aggregated.csv', parse_dates=['Date'])

# Bagian 2 -- Melakukan filter data untuk mengesktrak data Indonesia
data_indo = df[df["Country"] == "Indonesia"]

# Bagian 3 -- Melakukan filter data untuk data Malaysia dan Indonesia
negara = ["Indonesia", "Malaysia", 'Singapore']
ims_data = df[df["Country"].isin(negara)]

# Bagian 4 -- alternatif lain menggantikan cara pada bagian 3
alt_data = df[(df["Country"] == 'Indonesia') | (df['Country'] == 'Malaysia') |
              (df['Country'] == 'Singapore')]

covid19 = ims_data.pivot(index='Date', columns='Country', values='Confirmed')

plt.style.use('fivethirtyeight')
plt.figure(dpi=200)
plot = covid19.plot(figsize=(12, 8), linewidth=5, legend=False, ax=plt.gca())
plot.set_xlabel('Dates')
plot.set_ylabel('# of Infected')

# Section 8 - Assigning Colour
for country in negara:
    plot.text(x=covid19.index[-1], y=covid19[country].max(), s=country,
              weight='bold')

df.to_excel('covid19.xlsx', sheet_name='COVID19 Data', index=False)
plt.savefig("COVID19.png")
