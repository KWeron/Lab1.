import time

ileCzekać=int(input("Podaj przez jaki czas bedzie wyświetlał liczbę sekund: "))

for i in range(ileCzekać, 0, -1):
    print(i)
    time.sleep(1)
print("Minął czas oczekiwnia.")