#zad.9
def fun(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return (((1+(5**0.5))**n)-((1-(5**0.5))**n))/((2**n)*(5**0.5))

n=int(input("Podaj, który n-ty wyraz ciągu Fibonacciego ma zostać obliczony: "))
print(fun(n))