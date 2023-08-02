from pylab import*
"""
#konstanter
gamma = 6.67*10**(-11) #gravitasjonskonstanten Nm^2/kg^2
M = 5.97*10**24 #massen til jorda, kg
R = 6.37*10**6 #radius til jorda, m
 


#variable krefter, utregning av akselerasjon (gravitasjonsfeltstyrken)
def akselerasjon(s):
    a = -gamma*M/s**2
    return a

#startverdier
s = 3*R #startposisjon, m
v = 0   #startfarten, m/s
t = 0   #tiden
dt = 0.1 #tidssteg for simuleringen, s

#simulering av bevegelsen, fall mot jorden

while s > R:
    s = s-v*dt #beregner ny posisjon
    v = v+akselerasjon(s)*dt #beregner ny fart
    t = t+dt #tiden økes med dt

print(t/60, "minutter") #printer tiden det tar i minutter


"""
#annen løsning:

gamma = 6.67*10**(-11) #gravitasjonskonstanten Nm^2/kg^2
M = 5.97*10**24 #massen til jorda, kg
R = 6.37*10**6 #radius til jorda, m

x = 3*R #startposisjon, m
v = 0   #startfarten, m/s
t = 0   #tiden
dt = 0.1 #tidssteg for simuleringen, s

def g(r):
    return gamma*M/r**2 #m/s^2 Gravitasjonsfeltstyrken

while x>R:  #så lenge avstanden x er større enn jordradius
    x = x-v*dt #avstanden til jorda minker, beregner ny posisjon
    v = v+g(x)*dt #farten v øker, beregner ny fart
    t = t+dt #tiden økes med dt

print(t/60, "minutter") #printer tiden det tar i minutter







