
#funksjonen
def f(x):
    return 2*x**3-3*x**2-5*x+7

#den deriverte
def der(f, a, dx):
    return (f(a+dx)-f(a))/dx

derivert = der(f, -2,1e-8)

print(derivert)