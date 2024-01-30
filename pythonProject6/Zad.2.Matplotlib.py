import matplotlib.pyplot as plt

kategorie = ['Warzywa', 'Nabiał', 'Pieczywo', 'Produkty suche']
udzial = [12, 30, 28, 30]
plt.pie(udzial, labels=kategorie,
autopct='%1.f%%', startangle=90,
colors=['lightblue', 'lightgreen',
'coral', 'pink'])
plt.title('Udział w kategoriach')
plt.show()