m_lodd = 2.0    #kg
m_sloyfe = 0.25 #kg
L = 0.20        #m
g = 9.81        #m/s^2
B = 0.2         #T
R = 0.040       #ohm

s = 0           #startposisjon
v = 0           #startfart
t = 0           #tid
dt = 0.001      #tidssteg

a0 = 8.7 #m/s^2 Akselerasjonen før magnetfeltet

def a (v):
    Fm = ((v*B*L)/R)*L*B    #finner den magnetiske kraften. 
    aks = ((m_lodd*g)-Fm)/m_sloyfe+m_lodd  #finner akselerasjonen
    return(aks)

while s < 0.20:
    s = s+v*dt 
    v = v+a0*dt
    t = t + dt

while s<0.40:
    s = s + v * dt
    v = v + a(v) *dt
    t = t + dt

print("tiden vogna bruker er", t,"sekunder")

