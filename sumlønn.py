#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 21:06:45 2022

@author: majamarjamaa


Tenk deg at du får tilbud om å ta en sommerjobb. Arbeidsgiveren er litt rar, og sier at du får 1 krone den første dagen du jobber. Så dobler han daglønna di for hver dag du er på jobb. Det vil si at du får to kroner den andre dagen du jobber, 4 kroner den tredje dagen og så videre.
	Vi kan si at lønna di en bestemt dag, dag n, er et ledd i ei geometrisk rekke der     og   . Lønna på dag  n  er altså   .
	Samlet lønn for den første uka (fem arbeidsdager) blir da 
	 
	Lønna den første uka blir på bare 31 kr!

	Oppgave:
Lag et program som regner ut hvor mye du vil tjene til sammen på de 20 første arbeidsdagene med denne ordningen, dvs. finne summen av de 20 første leddene av rekka     ved hjelp av den eksplisitte formelen for   .

"""
lonn = 0
dager = 20

for n in range(1,dager+1):
    lonn = lonn + 2**(n-1)

print("Samlet lønn blir", lonn, "kr.")

