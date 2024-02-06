def main():
    try:
        a = int(input("Podaj początek przedziału (a): "))
        b = int(input("Podaj koniec przedziału (b): "))

        print(f"Liczby podzielne przez 3 z przedziału [{a}, {b}]:")
        for liczba in range(a, b + 1):
            if liczba % 3 == 0:
                print(liczba)

    except ValueError:
        print("Podane wartości muszą być liczbami całkowitymi.")
    except Exception as e:
        print(f"Wystąpił błąd: {e}")

if __name__ == "__main__":
    main()
