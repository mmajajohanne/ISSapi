#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 16:42:01 2021

@author: majamarjamaa
"""


from pylab import*

xmin = -10                                  #Setter en nedre grense for x-verdier
xmax = 10                                   #Setter en øvre grense for x-verdier
antall_punkter = 100                        #Definerer antallet punkter i listen
x_val = linspace(xmin,xmax,antall_punkter)  #Lager en liste med 100 punkter på x-verdier mellom -10 og 10


dx  = 1E-4

def f(x):
    return ((-x**3)+(8*x**2)-(2*x)+10)      #funksjonen 

def df(x):          
    return ((-3*x**2)+(16*x)-2)             #analytisk derivert

def fwd(x):
    return (f(x+ dx)-f(x))/dx               #funksjon foroverkvotient

def sym(x):
    return (f(x+dx)-f(x-dx))/(2*dx)         #funksjon symmetrisk kvotient


#regner ut og legger inn veridene for de deriverte i lister 
analytisk_y = df(x_val)
forkvotient_y = fwd(x_val)
symmetrisk_y = sym(x_val)


#halveringsmetoden for å finne nullpunktene til den deriverte (m verdiene fra forkvotient)
a = 0
b = 2

noyaktighet = 1E-3
m = (a+b)/2

while abs(fwd(m)) >= noyaktighet:
    if fwd(a)*fwd(m)<0:
        b = m
    else:
        a = m
    m = (a+b)/2

print("nullpunkt nr 1 til den foroverderiverte er", round(m,4))

c = 2.5
d = 10

m2 = (c+d)/2

while abs(fwd(m2)) >= noyaktighet:
    if fwd(c)*fwd(m2)<0:
        d = m2
    else:
        c = m2
    m2 = (c+d)/2

print("nullpunkt nr 2 til den foroverderiverte er", round(m2,4))


#underersøker om det stasjonære punktet er et topppunkt eller et bunnpunkt
#stasjonært punkt 1
ut=(fwd(m-0.01))
ut2=(fwd(m+0.01))

if ut<0 and ut2>0:
    print ("nullpunkt 1 er bunnpunkt")
elif (ut<0 and ut2<0) or (ut>0 and ut2>0):
    print ("nullpunktet er et terrassepunkt")
else: 
    print ("nullpunkt 1 er toppunkt")

#stasjonært punkt 2
un=(fwd(m2-0.01))
un2=(fwd(m2+0.01))

if un<0 and un2>0:
    print ("nullpunkt 2 er bunnpunkt")
elif (un<0 and un2<0) or (un>0 and un2>0):
    print ("nullpunktet er et terrassepunkt")
else: 
    print ("nullpunkt 2 er toppunkt")
    
    


#finner differansen mellom de ulike versjonene av den deriverte
sumA = sum(analytisk_y)                     #summerer listen med verdier av den analytiske deriverte
sumFo = sum(forkvotient_y)                  #summerer listen med verdier av forkvotienten
dif = sumA-sumFo                            #finner differansen mellom summen analytisk og forkvotient


sumSy = sum(symmetrisk_y)                   #summerer listen med verdier av den symmetriske kvotienten
dif2 = sumA-sumSy                           #finner differansen mellom summen av analytisk og symmetrisk kvotient
    
#print ("absoluttverdien til differansen mellom analytisk og forkvotient er", abs(dif))          #printer absoluttverdien av differansen
#print ("absoluttverdien til differansen mellom analytisk og symmetrisk kvotient er", abs(dif2)) #printer absoluttverdien av differansen



#plotter grafene
plot(x_val, analytisk_y, label="f'(x) analytisk", color="m")                           #tegner grafen til den analytisk deriverte med farge magenta
plot(x_val, forkvotient_y, label="f'(x) newtons kvotient" , color="y")                 #tegner grafen til forkvotienten (newtons kvotient) med farge grønn
plot (x_val, symmetrisk_y, label="f(x) newtons symmetriske kvotient", color="orange")  #tegner grafen til den symmetrike kvotienten med farge oransje

title("dx = 10^(-4)")                                                                      #setter tittel på grafen
ylim(-500, 100)                                                                        #setter en fast grense for y-aksen 
legend()                                                                               #viser navnene til grafene
grid()                                                                                 #viser rutenett
show()                                                                                 #viser grafene

