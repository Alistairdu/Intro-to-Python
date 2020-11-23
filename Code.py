from math import e, factorial
from scipy.stats import poisson


def geo(k,p): # first success is on kth trial
    return (1-p)**(k-1) * p

def geo_cdf(k,p):
    return sum([geo(i,p) for i in range(1,k+1)])

def geo_cdff(k,p):
    return 1-(1-p)**k

def poisson2(lamb,k):
    return lamb**k * e**-lamb / factorial(k)

def poisson_cdf(lamb,k):
    return sum([poisson(lamb,i) for i in range(k+1)])

def poisson_mv(lam):
    return lam, lam

lamb = 20
k = 25
# p = 0.00016

print(poisson.pmf(k=25,mu=20))

# def geo_mv(p):
#     return 1/p, (1-p)/p**2

