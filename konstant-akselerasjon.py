
#konstant akselerasjon 
from pylab import*

#informasjon om bevegelsen
s = 0.0 #startposisjon, m
v = 0.0 #startfart, m/s
a = 25.0 #akselerasjon, m/s^2
t = 0.0 #starttid, s

#simuneringsteknisk
t_slutt = 20.0 #sluttid, s
dt = 0.1 #lengde på tidssteg i s, nøyaktighet
t_verdier = [t] #loste hvor verdiene av t legges inn
s_verdier = [s] #loste hvor verdiene av s legges inn

#løkka regner ut ny posisjon for hvert tidssteg
while t < t_slutt:
    v = v + a * dt  #beregner ny fart
    s = s + v * dt  #beregner ny posisjon
    t = t + dt      #tiden økes med dt
    t_verdier.append(t) #legger til t inn i tidslisten
    s_verdier.append(s) #legger s inn i posisjonslisten
    
#tegner graf
plot (t_verdier, s_verdier)     #lager grafen
title ("Strekning som funksjon av tid") #tittel på grafen
xlabel("$t$ (s)")   #x-akse tittel (dollar gir kursiv)
ylabel ("$s$ (m)") #y-akse tittel 
grid() #legger til rutenett
show() #viser grafen
    
    
    


