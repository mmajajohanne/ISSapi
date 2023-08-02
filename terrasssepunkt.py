#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 08:21:40 2021

@author: majamarjamaa
"""

from pylab import*

xmin = -10                                  #setter en nedre grense for x-verdier
xmax = 10                                   #setter en øvre grense for x-verdier
antall_punkter = 100                        #definerer antallet punkter i listen
x_val = linspace(xmin,xmax, antall_punkter) #lager en liste med 100 punkter på x-.verdier mellom -10 og 10

dx = 1E-4

def f(x):                                   #funksjon med terrassepunkt
    return (x**3+4)

def fwd(x):                                 #funksjon forkvotient derivert
    return (f(x+dx)-f(x))/dx

forkvotient_y = fwd(x_val)
funksjon_y = f(x_val)

#halveringsmetoden for å finne nullpunktene til den deriverte
a = -10
b = 10

noyaktighet = 1E-3
m = (a+b)/2

while abs(fwd(m))>= noyaktighet:
    if fwd(a)*fwd(m)<0:
        b = m
    else:
        a = m
    m = (a+b)/2

print ("nullpunktet til den foroverderiverte er", round(m,4))

#undersøker hvilken type stasjonært punkt det er
ut = (fwd(m-0.01))
ut2 = (fwd(m+0.01))

if ut<0 and ut2>0:
    print ("nullpunkt er bunnpunkt")
elif (ut>0 and ut2>0) or (ut2<0 and ut2<0):
    print ("nullpunkt er terrassepunkt")
else:
    print ("nullpunkt er toppunkt")

#plotter funksjonen og den deriverte
plot(x_val, funksjon_y, label="funskjon f(x)", color="blue")
legend()
grid()
show()
    