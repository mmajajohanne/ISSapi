#oppgave 7 fysikk

from pylab import*
#informasjon om bevegelsen
s = 0 #startposisjon, m
v = 0 #startfart, m/s
t = 0 #starttid, s

# Simuleringsteknisk
s_slutt = 0.40 #sluttposisjon, m
dt = 0.0001 #lengde på tidssteg, s

def a(s): #akselerasjonen er en funksjon av posisjon
    aks = 300/(s + 0.01) #beregner akselerasjonen
    return aks

#løkka regner ut ny akselerasjon, fart og posisjon
while s < s_slutt:
    v = v + a(s)*dt #beregner ny fart
    s = s + v*dt #beregner ny posisjon
    t = t + dt #øker tiden med dt
    
#skriver ut sluttfart
print ("fart:", v-v*dt, "m/s")
