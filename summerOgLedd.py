#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 21:08:59 2022

@author: majamarjamaa

a	Leddene i ei uendelig rekke er gitt ved formelen   .
			Lag et program som skriver ut de 20 første leddene.

b	Utvid programmet slik at det også skriver ut de 20 første summene, det vil si og så videre.

"""

#a
a_n = 0
antall = 1
Leddene = []

for n in range(1,21):
    a_n = 1/(1+n)**2
    Leddene.append(a_n)
    antall = antall+1

print(Leddene)


#b
a_n = 0
Sum = 0
antall = 1
Leddene = []
Summene = []

for n in range(1,21):
    a_n = 1/(1+n)**2
    Sum = Sum + a_n
    Leddene.append(a_n)
    Summene.append(Sum)
    antall = antall+1

print(Leddene)
print(Summene)
