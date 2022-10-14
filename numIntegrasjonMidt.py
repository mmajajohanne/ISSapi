# coding=utf-8
#%%
""" Funksjonen f er gitt ved f(x) = x**(2*x)
      Lag et program som finner en tilnærmingsverdi for integralet f(x)dx i intervallet [1,5]
      Bruk rektangelmetoden med midtpunkttilnærming med 20 rektangler 

a = 1       #øvre grense i intervallet
b = 5       #nedre grense i intervallet
n = 20      #antall rektangler

def f(x):
    return x**(2*x)

summen = 0
delta_x = (b-a)/n   #rektangelbredden

for i in range(n):  #i fra og med 0 til og med n-1
    summen = summen + f((a + 0.5 * delta_x) + i * delta_x) * delta_x

print(round(summen,2))

"""

#%%

"""
     2.22 Finn integralet av sqrt(4-x**2) i intervallet [-2,2] med 10 rektangler
"""

a = -2
b = 2
n = 10

def f(x):
    return (4-(x**2))**(0.5)

summen = 0
delta_x = (b-a)/n

for i in range(n):
    summen = summen + f((a + (0.5+i) * delta_x)) * delta_x      #fasiten sier dette er riktig metode

print(round(summen,2))