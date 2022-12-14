x = [1,5,]
y = [14,20]

a = 0   #øvre grense
b = 10   #nedre grense
n = 5   #delintervaller
trapessummen = x[1]-x[0]

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