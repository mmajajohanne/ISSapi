#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 10:37:51 2021

@author: majamarjamaa
"""
import matplotlib.pyplot as plt 

#definerer massen til a og b
Ma = 4
Mb = 2

#setter startsposisjon for a og b
Sa0 = 0
Sb0 = 5

#setter fart for a og b før støtet
Va0 = 4
Vb0 = 0 
P0 = Ma*Va0 + Mb*Vb0

#regner ut farten til a og b etter støtet
Vb = (Ma*Va0 + P0 - Ma * Vb0)/(Ma+Mb)
Va = (P0-Mb*Vb)/Ma

t = 0
dt = 0.01

Sa = Sa0
Sb = Sb0
SbListe = []
SaListe = []
tidListe = []

while Sa < Sb:
    Sa += Va0 * dt
    Sb += Vb0 * dt
    t += dt
    
    SbListe.append(Sb)
    SaListe.append(Sa)
    tidListe.append(t)
    
    

for i in range (200):
    Sa += Va * dt
    Sb += Vb * dt
    t += dt
    
    SbListe.append(Sb)
    SaListe.append(Sa)
    tidListe.append(t)
    

#lager en tom graf
graf = plt.axes( )
#velger hva som skal plottes i grafen
graf.plot(tidListe, SaListe)
graf.plot(tidListe, SbListe)

    

