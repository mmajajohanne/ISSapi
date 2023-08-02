from pylab import *

#regne fart tid osv python

#startsbetingelser
v = 5
s = 0
t = 0
a = 2

t_slutt = 3.0
dt = 0.1                #(endring i tid for hver gang programmet skal regne ny strekning)

#for å lage graf må vi ha lister for t-o g s-verdier
t_verdier = [t]
s_verdier = [s]


while t < t_slutt:
    s = s + v*0.1
    v = v + a * dt
    t = t + dt
    t_verdier.append(t)
    s_verdier.append(s)


plot(t_verdier, s_verdier)
title ("Strekning som funksjon av tid")


#print (f' "etter {t_slutt} sekunder har vi beveget oss {s} meter")
    