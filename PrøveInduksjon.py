from pylab import *
t = 0
dt = 0.0001
g = 9.81
k = 4.878
s = 0
v = 0
e = 0
eListe = []
tListe = []
B = 0.50
L = 0.2
IListe = []
R = 0.041

while s <= 1.2:
    f1 = (B*L*s)
    t1 = t
    s = s + v*dt
    a = g - k*v
    v = v + a*dt
    t = t + dt
    #e = ((B*L*s)-f1)/(t-t1)
    e = v*B*L
    eListe.append(e)
    tListe.append(t)

    I = e/R
    IListe.append(I)   
print(e, s)


plot(tListe,eListe)
title("Indusert spenning i sløyfa fra fallet starter til den er ute av magnetfeltet")
xlabel("Tid(s)")
ylabel("Ems(V)")
show()
"""
plot(tListe,IListe)
title("Graf for strømmen i sløyfa")
xlabel("Tid(s)")
ylabel("I(A)")
show()"""