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
cured = df.pivot(index='Date', columns='Country', values='Recovered')
death = df.pivot(index='Date', columns='Country', values='Deaths')
frate = df.pivot(index='Date', columns='Country', values='FRates')
crate = df.pivot(index='Date', columns='Country', values='CRates')

plt.style.use('fivethirtyeight')
plt.figure(num=1, dpi=200)
plot = covid19.plot(grid=False, fontsize=15, figsize=(12, 8),
                    linewidth=5, legend=False, ax=plt.gca())
plot.grid(b=True, which='major', axis='y', ls='--', lw=.5, c='k', alpha=.3)
plot.set_title("COVID-19 Confimed Case", fontweight='bold', loc='center')
plot.set_xlabel('Dates')
plot.set_ylabel('# of Infected')
for country in negara:
    plot.text(x=covid19.index[-1], y=int(covid19[country].tail(1)),
              s=country+": "+str(int(covid19[country].tail(1))),
              fontsize=15)
plot.text(x=covid19.index[1], y=-1850, s='Source: https://github.com/datasets/\
covid-19/blob/master/data/countries-aggregated.csv', fontsize=12,
          fontweight='bold')
plot.text(x=covid19.index[1], y=-2100, s="by: GSK", fontsize=12,
          fontweight='bold')
plt.savefig('Infected Number.png', bbox_inches="tight")


plt.figure(num=2, dpi=200)
plot = death.plot(grid=False, fontsize=15, figsize=(12, 8), linewidth=5,
                  legend=False, ax=plt.gca())
plot.grid(b=True, which='major', axis='y', ls='--', lw=.5, c='k', alpha=.3)
plot.set_title("COVID-19 Total Death", fontweight='bold', loc='center')
plot.set_xlabel('Dates')
plot.set_ylabel('# of Death')
for country in negara:
    plot.text(x=death.index[-1], y=int(death[country].tail(1)),
              s=country+": "+str(int(death[country].tail(1))),
              fontsize=15)
plot.text(x=covid19.index[1], y=-160, s='Source: https://github.com/datasets/\
covid-19/blob/master/data/countries-aggregated.csv', fontsize=12,
          fontweight='bold')
plot.text(x=covid19.index[1], y=-180, s="by: GSK", fontsize=12,
          fontweight='bold')
plt.savefig('Death Number.png', bbox_inches="tight")


plt.figure(num=5, dpi=200)
plot = cured.plot(grid=False, fontsize=15, figsize=(12, 8), linewidth=5,
                  legend=False, ax=plt.gca())
plot.grid(b=True, which='major', axis='y', ls='--', lw=.5, c='k', alpha=.3)
plot.set_title("COVID-19 Total Recovered", fontweight='bold', loc='center')
plot.set_xlabel('Dates')
plot.set_ylabel('# of Recovered')
for country in negara:
    plot.text(x=cured.index[-1], y=int(cured[country].tail(1)),
              s=country+": "+str(int(cured[country].tail(1))),
              fontsize=15)
plot.text(x=covid19.index[1], y=-160, s='Source: https://github.com/datasets/\
covid-19/blob/master/data/countries-aggregated.csv', fontsize=12,
          fontweight='bold')
plot.text(x=covid19.index[1], y=-180, s="by: GSK", fontsize=12,
          fontweight='bold')
plt.savefig('Cured Number.png', bbox_inches="tight")


plt.figure(num=3, dpi=200)
plot = frate.plot(grid=False, fontsize=15, figsize=(12, 8), linewidth=5,
                  legend=False, ax=plt.gca())
plot.grid(b=True, which='major', axis='y', ls='--', lw=.5, c='k', alpha=.3)
plot.set_title("COVID-19 Fatality Rate", fontweight='bold', loc='center')
plot.set_xlabel('Dates')
plot.set_ylabel('Fatality Rate (%)')
for country in negara:
    plot.text(x=frate.index[-1], y=float(frate[country].tail(1)),
              s=country+": "+str(float("%.2f" % frate[country].tail(1)))+'%',
              fontsize=15)
plot.text(x=covid19.index[1], y=-2.5, s='Source: https://github.com/datasets/\
covid-19/blob/master/data/countries-aggregated.csv', fontsize=12,
          fontweight='bold')
plot.text(x=covid19.index[1], y=-2.8, s="by: GSK", fontsize=12,
          fontweight='bold')
plt.savefig('Fatality Rate.png', bbox_inches="tight")


plt.figure(num=4, dpi=200)
plot = crate.plot(grid=False, fontsize=15, figsize=(12, 8), linewidth=5,
                  legend=False, ax=plt.gca())
plot.grid(b=True, which='major', axis='y', ls='--', lw=.5, c='k', alpha=.3)
plot.set_title("COVID-19 Recovered Rate", fontweight='bold', loc='center')
plot.set_xlabel('Dates')
plot.set_ylabel('Recovered Rate (%)')
for country in negara:
    plot.text(x=crate.index[-1], y=float(crate[country].tail(1)),
              s=country+": "+str(float("%.2f" % crate[country].tail(1)))+'%',
              fontsize=15)
plot.text(x=covid19.index[1], y=-2.5, s='Source: https://github.com/datasets/\
covid-19/blob/master/data/countries-aggregated.csv', fontsize=12,
          fontweight='bold')
plot.text(x=covid19.index[1], y=-2.8, s="by: GSK", fontsize=12,
          fontweight='bold')
plt.savefig('Recovered Rate.png', bbox_inches="tight")
