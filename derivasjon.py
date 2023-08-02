from pylab import*

delta_x = 1E-8

#funksjonen
def f(x):
    return x**2 + 2*x

#analytisk derivasjon
def ander (a):
    return (2*a+2)

#newtons kvotient 
def numder(a):
    return (f(a+ delta_x)-f(a))/delta_x

#newtons symmetriske kvotient
def nskder(a):
    return (f(a+delta_x)-f(a-delta_x))/(2*delta_x)

x_verdier = linspace(-5,5,100)
y_verdier = f(x_verdier)
ay_verdier = ander(x_verdier)
dy_verdier = numder(x_verdier)
nsky_verdier = nskder(x_verdier)


plot(x_verdier, y_verdier, label="f(x)", color="c")
plot(x_verdier, ay_verdier, label="f'(x) analytisk", color="m")
plot(x_verdier, dy_verdier, label="f'(x) newtons kvotient" , color="y")
plot (x_verdier, nsky_verdier, label="f(x) newtons symmetriske kvotient", color="orange")

legend()
grid()
show()