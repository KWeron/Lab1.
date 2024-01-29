import pandas as pd

data = {'Nr albumu': ['34256', '25345', '52048', '12423'],
        'Imię': ['Anna', 'Jan', 'Katarzyna', 'Tomasz'],
        'Nazwisko': ['Kowalska', 'Nowak', 'Lis', 'Tarnowski'],
        'Wiek': [20, 19, 28, 21],
        'Ocena': [2.0, 5.0, 3.5, 4.0]}

df = pd.DataFrame(data)
print(df)

# a
print(df[df['Ocena'] > 4.0])

for row in df.itertuples():
    if row.Ocena > 4.0:
        print(row.Ocena, row.Imię)

# b
print(df.sort_values('Ocena'))

# c
print(df.groupby('Ocena').get_group(5.0))
print(df.groupby('Ocena')['Wiek'].min())

# d
dataPop = {'Nr albumu': ['34256', '36573'],
'Imię': ['Anna', 'Kamil'],
'Nazwisko': ['Kowalska', 'Wójcik'],
'Wiek': [20, 25],
'Ocena': [4.5, 4.0]}
df_pop = pd.DataFrame(dataPop)
print(df_pop['Ocena'])
print(pd.merge(df, df_pop, on='Nr albumu', how='outer'))

#e
print(df.to_csv('df.csv', index=False))

#f
print(pd.read_csv)

#g
dodStudenta={'Nr albumu': '23459',
             'Imię': 'Oliwia',
             'Nazwisko': 'Reja',
             'Wiek': 27,
             'Ocena': 4.5}

df.loc[len(df)] = dodStudenta
print(df)

#h
print(df['Ocena'].unique())

#i
oceny = df['Ocena'].value_counts()
ileOsob5 = oceny.get(5, 0)
print(ileOsob5)