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


dx  = 1E-19

def f(x):
    return ((-x**3)+(8*x**2)-(2*x)+10)      #funksjonen 

def df(x):          
    return ((-3*x**2)+(16*x)-2)             #analytisk derivert

def fwd(x):
    return (f(x+ dx)-f(x))/dx               #funksjon foroverkvotient

def sym(x):
    return (f(x+dx)-f(x-dx))/(2*dx)         #funksjon symmetrisk kvotient




analytisk_y = df(x_val)
forkvotient_y = fwd(x_val)
symmetrisk_y = sym(x_val)


#print("Analytisk:", analytisk_y)
#print("Forkvotient:", forkvotient_y)
#print("Symmetrisk:", symmetrisk_y)


#oppgave g)
sumA = sum(analytisk_y)                     #summerer listen med verdier av den analytiske deriverte
sumFo = sum(forkvotient_y)                  #summerer listen med verdier av forkvotienten
dif = sumA-sumFo                            #finner differansen mellom summen analytisk og forkvotient


sumSy = sum(symmetrisk_y)                   #summerer listen med verdier av den symmetriske kvotienten
dif2 = sumA-sumSy                           #finner differansen mellom summen av analytisk og symmetrisk kvotient
    
print ("absoluttverdien til differansen mellom analytisk og forkvotient er", abs(dif))          #printer absoluttverdien av differansen
print ("absoluttverdien til differansen mellom analytisk og symmetrisk kvotient er", abs(dif2)) #printer absoluttverdien av differansen



#oppgave f
plot(x_val, analytisk_y, label="f'(x) analytisk", color="m")                           #tegner grafen til den analytisk deriverte med farge magenta
plot(x_val, forkvotient_y, label="f'(x) newtons kvotient" , color="y")                 #tegner grafen til forkvotienten (newtons kvotient) med farge grønn
plot (x_val, symmetrisk_y, label="f(x) newtons symmetriske kvotient", color="orange")  #tegner grafen til den symmetrike kvotienten med farge oransje

title("dx = 10^(-19)")                                                                      #setter tittel på grafen
ylim(-500, 100)                                                                        #setter en fast grense for y-aksen 
legend()                                                                               #viser navnene til grafene
grid()                                                                                 #viser rutenett
show()                                                                                 #viser grafene

