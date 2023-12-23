listaZakupow = {"kalendarz": 25.78, "serek na kanape": 4.56, "cebula": 2.54, "makaron": 5.99, "zabawka": 120.35}
print(listaZakupow)
suma=0

for key in listaZakupow:
    suma+= listaZakupow[key]
    print(key)
    print(suma)

print(suma)