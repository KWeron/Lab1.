def czy_podzielne_przez_3(a):
    return a % 3 == 0

# Testowanie funkcji
liczba_testowa = 9  # Możesz zmienić wartość liczba_testowa na dowolną liczbę do przetestowania
wynik_testu = czy_podzielne_przez_3(liczba_testowa)

if wynik_testu:
    print(f"Liczba {liczba_testowa} jest podzielna przez 3.")
else:
    print(f"Liczba {liczba_testowa} nie jest podzielna przez 3.")
