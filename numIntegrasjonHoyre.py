# coding=utf-8
""" Funksjonen f er gitt ved f(x) = x**2 - 2x + 2
      Lag et program som finner en tilnærmingsverdi for integralet f(x)dx i intervallet [1,5]
      Bruk rektangelmetoden med høyre med ti rektangler """

a = 1       #øvre grense i intervallet
b = 5       #nedre grense i intervallet
n = 10      #antall rektangler

def f(x):
    #return x**2 - 2*x + 2
    return x**(2*x)

summen = 0
delta_x = (b-a)/n   #rektangelbredden

for i in range(1,n+1):  #i fra og med 0 til og med n-1
    summen = summen + f(a + i*delta_x) * delta_x #endring her?

print(round(summen,2))
