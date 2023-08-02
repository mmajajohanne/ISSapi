from pylab import *

def f(x):                                           
    return 350*1.2**x-756


#print(f(0))
#print (f(5))

a = 0                                               
b = 5
nøyaktighet = 0.0001


m = (a+b)/2


while abs(f(m)) >= nøyaktighet:
    if f(a)*f(m) < 0:
        b = m
    else:
        a = m
        
    m = (a+b)/2

print("løsningen på likningen er tilnærmet lik", round(m,4))