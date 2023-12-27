slownik = {'sierpien': 98.12, 'wrzesien': 120.53, 'pazdziernik': 100.47, 'listopad': 112.98, 'grudzien': 160.83}

#a
maxWartosc = max(slownik.values())
print("Najwięcej zostało zapłacone: ",maxWartosc)

minWartosc = min(slownik.values())
print("Najmniej zostało załpacone: ",minWartosc)

sumaWartosc = sum(slownik.values())
print("Łącznie wydano na rachunki za prąd: ",sumaWartosc)

sredniaWartosc = sumaWartosc/len(slownik)
print("Średnio wydano na rachunki: ",sredniaWartosc)

#b
ostatniMiesiac = list(slownik.keys())[-1]
woMiesiac = slownik[ostatniMiesiac]
if woMiesiac>sredniaWartosc:
    print("Zacznij oszczędać!!!")
else:
    print("Jest dobrze!!!")