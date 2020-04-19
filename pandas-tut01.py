import pandas as pd
import matplotlib.pyplot as plt

# Bagian 1 -- Load data dari sumbernya
df = pd.read_csv(
    'https://raw.githubusercontent.com/datasets/covid-19/\
master/data/countries-aggregated.csv', parse_dates=['Date'])

# Bagian 2 -- Melakukan filter data untuk data Malaysia dan Indonesia
negara = ["Indonesia", "Malaysia", 'Singapore']
df = df[df["Country"].isin(negara)]
# Bagian 3 -- Menambahkan kolom total Case, fatality rate, dan cure rate
df['Cases'] = df.iloc[:, 2:5].sum(axis=1)
df['FRates'] = ((df['Deaths']/df['Cases'])*100).fillna(0)
df['CRates'] = ((df['Recovered']/df['Cases'])*100).fillna(0)

covid19 = df.pivot(index='Date', columns='Country', values='Confirmed')
death = df.pivot(index='Date', columns='Country', values='Deaths')
frate = df.pivot(index='Date', columns='Country', values='FRates')
crate = df.pivot(index='Date', columns='Country', values='CRates')

plt.style.use('fivethirtyeight')
plt.figure(dpi=200)
plot = covid19.plot(title="COVID-19 Infection Number", fontsize=15,
                    figsize=(12, 8), linewidth=5, legend=True, ax=plt.gca())
plot.set_xlabel('Dates')
plot.set_ylabel('# of Infected')
for country in negara:
    plot.text(x=covid19.index[-1], y=int(covid19[country].tail(1)),
              s=int(covid19[country].tail(1)), fontsize=15)

plt.figure(dpi=200)
plot = death.plot(title="COVID-19 Death Number", fontsize=15,
                  figsize=(12, 8), linewidth=5, legend=True, ax=plt.gca())
plot.set_xlabel('Dates')
plot.set_ylabel('# of Death')
for country in negara:
    plot.text(x=death.index[-1], y=int(death[country].tail(1)),
              s=int(death[country].tail(1)),
              fontsize=15)

plt.figure(dpi=200)
plot = frate.plot(title="COVID-19 Fatality Rate", fontsize=15,
                  figsize=(12, 8), linewidth=5, legend=True, ax=plt.gca())
plot.set_xlabel('Dates')
plot.set_ylabel('Fatality Rate')
for country in negara:
    plot.text(x=frate.index[-1], y=float(frate[country].tail(1)),
              s=float("%.2f" % frate[country].tail(1)),
              fontsize=15)

plt.figure(dpi=200)
plot = crate.plot(title="COVID-19 Cured Rate", fontsize=15,
                  figsize=(12, 8), linewidth=5, legend=True, ax=plt.gca())
plot.set_xlabel('Dates')
plot.set_ylabel('# of Death')
for country in negara:
    plot.text(x=crate.index[-1], y=float(crate[country].tail(1)),
              s=float("%.2f" % crate[country].tail(1)),
              fontsize=15)
