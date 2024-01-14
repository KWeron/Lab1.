def potegowanie(a, n):
  if n==0:
    return 1
  elif n>0:
    return a*potegowanie(a,n-1)
  else:
    return 1/(a*potegowanie(a,-n-1))

n=int(input("Podaj jaka jest wartość potęgi (n): "))
a=float(input("Podaj liczbę, która będzie potęgowana (a): "))
print(potegowanie(a,n))