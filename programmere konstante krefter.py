from pylab import plot, title, xlabel,ylabel, grid, show

#Informasjon om konstanter, krefter og gjenstanden
m = 5.0     #massen av gjenstanden, kg
g = 9.81     #tyngdeakselerasjon, m/s^s



sum_F = m*g #kraftsum, N
a = sum_F/m #akselerasjon, m/s^s

#startverdier for bevegelsen
s = 0
v = 0
t = 0

#simuleringsteknisk
t_slutt = 10        #sluttid for simulering, s
dt = 0.01           #lengde på tidssteg, s
s_verdier = [s]     #liste for lagring av posisjon
v_verdier = [v]     #liste for lagring av fart
t_verdier = [t]     #liste for lagring av tid

#løkke som beregner ny fart, posisjon og tid
while t < t_slutt:  #så lenge det ikke har gått 10 sekunder
    v = v + a*dt    #regner ut ny v og overskriver gammel
    s = s + v*dt    #regner ut ny s og overskriver gammel
    t = t + dt      #regner ut ny t og overskriver gammel

    t_verdier.append(t) #legger til ny t-verdi i listen for t
    v_verdier.append(v) #legger til ny v-verdi i listen for v
    s_verdier.append(s) #legger til ny s-verdi i listen for s

#Tegning av graf
plot(t_verdier, s_verdier)              #lager grafen
title("Strekning som funksjon av tid")  #tittel på grafen
xlabel("$t$ / s")                       #x-akse-tittel
ylabel("$s$ / m")                       #y-akse-tittel
grid()
show()
