import pandas as pd

df = pd.DataFrame({
    "Nama": ['Gilang Samudra', 'Fitria Malinda', 'Maryam Arisha'],
    "Usia": [31, 28, 1],
    "Berat Badan": [70,65,10]})

anggota = {"Nama": ['Gilang Samudra', 'Fitria Malinda', 'Maryam Arisha'],
           "Usia": [31, 28, 1],
           "Berat Badan": [70,65,10]}

maxi = df["Berat Badan"].max()
maxi2 = pd.Series(anggota["Berat Badan"]).max()
print(maxi)
print(maxi2)