
from pylab import *

s = 0.0
v = 0.0
a = 4.0
t = 0.0

t_slutt = 5.0
dt = 0.1
t_verdier = [t]
s_verdier = [s]

while t < t_slutt:
  v = v + a*dt
  s = s + v*dt
  t = t + dt
  t_verdier.append(t)
  s_verdier.append(s)
  
plot(t_verdier, s_verdier)
show()
  

from pylab import *
s = 0
v = 0
a = 4
t = 0
t_slutt = 5  # sluttid, s
dt = 0.01    # tidssteg, s
# startposisjon, m
# startfart, m/s
# akselerasjon, m/s^2
# starttid, s
t_verdier = [t]  # liste hvor verdiene av t legges inn
s_verdier = [s]  # liste hvor verdiene av s legges inn
v_verdier = [v]  # liste hvor verdiene av v legges inn
# Løkken regner ut ny fart, posisjon og tid for ballen
while t < t_slutt:
    