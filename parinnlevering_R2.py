#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 10:06:20 2022

@author: majamarjamaa

#oppgave 1
a1 = 1
k = 2

rekke = [] 

for i in range(1,21):
    a = 2**(i-1)    #finner de 20 første leddene i rekka
    rekke.append(a)

s = rekke[0] * ((rekke[19]-1) / (k-1)) #regner ut summmen av den geometriske rekka

print (s)
"""

#oppgave 2a
rekke = []

for i in range(1,21):
    a = 1 / ((1 + i)**2)    #finner de første 20 leddene i rekka
    rekke.append(a)

#print(rekke)



#2B
tall = 1
sum2 = 0
SumListe = []

while tall < len(rekke):
    for s in range(0,tall):
        sum2 = sum2 + rekke[s]
    SumListe.append(sum2)
    tall += 1
    
print(SumListe)
    



