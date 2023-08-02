#oppgave 3b del 2
g = 6.67*10**(-11)  #gravitasjonskonstant
rj = 6371*1000      #radius jordklokden, m
mj = 5.974*10**24   #jordmassen, kg
mk = 10             #kulemassen, kg

v = 313             #startfart, m/s
h = rj              #startposisjon, m
t = 0               #tid, s
dt = 0.001          #tidssteg

#regner ut tyngdeakselerasjonen
def a(h):
    return (g*mj/(h**2))

#finner tiden det tar å komme til det høyeste punktet
while v>0:
    h = h + v *dt
    v = v-a(h)*dt
    t = t + dt
#bevegelsen tar like lang tid begge veier (når man ser bort fra luftmotstand)
print("Bevegelsen tar", round(2*t,2), "s.")


