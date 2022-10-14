"""trapesmetoden for bestemt integral av funksjonen 1/(x+x**2) i intervallet [1,2]."""

a = 1   #øvre grense
b = 2   #nedre grense
n = 5   #delintervaller
trapessummen = 0

def f(x):
    return 1/(x+(x**2))

def trapesmetoden(a,b,n):
    summen = 0
    dx = (b-a)/n
    
    for i in range(1, n):
        summen = summen + f(a + i*dx)
    trapessummen = dx/2*(2*summen+f(a)+f(b))
    return trapessummen

print(round(trapesmetoden(a,b,n),2))

