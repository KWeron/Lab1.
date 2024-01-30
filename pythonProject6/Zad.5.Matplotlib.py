import matplotlib.pyplot as plt
import pandas as pd

data = {'Nr albumu': ['34256', '25345', '52048', '12423'],
        'Imię': ['Anna', 'Jan', 'Katarzyna', 'Tomasz'],
        'Nazwisko': ['Kowalska', 'Nowak', 'Lis', 'Tarnowski'],
        'Ocena1': [2.0, 5.0, 3.5, 4.0],
        'Ocena2': [4.5, 4.0, 4.0, 3.0],
        'Ocena3': [3.5, 4.5, 4.0, 5.0]}

df = pd.DataFrame(data)
ocenaKolos1=df['Ocena1']
ocenaKolos2=df['Ocena2']
ocenaKolos3=df['Ocena3']
nrAlbumu=df['Nr albumu']

#a
plt.figure()
plt.plot(nrAlbumu, ocenaKolos1, label='Ocena1')
plt.title('Ocena z pierwszego terminu')
plt.xlabel('Nr albumu')
plt.ylabel('Ocena')
plt.legend()
plt.grid(True)
plt.show()

plt.figure()
plt.plot(nrAlbumu, ocenaKolos2, label='Ocena2')
plt.title('Ocena z drugiego terminu')
plt.xlabel('Nr albumu')
plt.ylabel('Ocena')
plt.legend()
plt.grid(True)
plt.show()

plt.figure()
plt.plot(nrAlbumu, ocenaKolos3, label='Ocena3')
plt.title('Ocena z trzeciego terminu')
plt.xlabel('Nr albumu')
plt.ylabel('Ocena')
plt.legend()
plt.grid(True)
plt.show()

plt.figure()
plt.plot(nrAlbumu, ocenaKolos1, label='Ocena1')
plt.plot(nrAlbumu, ocenaKolos2, label='Ocena2')
plt.plot(nrAlbumu, ocenaKolos3, label='Ocena3')
plt.title('Ostateczny rokład ocen z poszczególnych terinów')
plt.xlabel('Nr albumu')
plt.ylabel('Ocena')
plt.legend()
plt.grid(True)
plt.show()

#b
plt.figure()
plt.plot(nrAlbumu, ocenaKolos1, label='Ocena1',  marker='o', linestyle=':', color='gold', linewidth=2, alpha=0.8)
plt.plot(nrAlbumu, ocenaKolos2, label='Ocena2',  marker='s', linestyle='-', color='pink', linewidth=2, alpha=0.8)
plt.plot(nrAlbumu, ocenaKolos3, label='Ocena3',  marker='^', linestyle='-.', color='lightgreen', linewidth=2, alpha=0.8)
plt.title('Ostateczny rokład ocen z poszczególnych terinów')
plt.xlabel('Nr albumu')
plt.ylabel('Ocena')
plt.legend()
plt.grid(True)
plt.show()
