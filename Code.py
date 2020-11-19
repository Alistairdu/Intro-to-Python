from math import e, sqrt
from random import random, choice


def factorial(n):
    prod = 1
    for i in range(2,n+1):
        prod *= i
    return prod

def permutation(n,k):
    return int(Stats.factorial(n) / Stats.factorial(n-k))

def combination(n,k):
    return int((Stats.permutation(n,k)/ Stats.factorial(k)))

def bernoulli(p):
    if random()<p:
        return 1
    return 0

def binomial(n,k,p=0.5):
    return Stats.combination(n,k) * p**k * (1-p)**(n-k)

def binomial_cdf(n,k,p):
    return sum([Stats.binomial(n, i, p) for i in range(k+1)])

def binomial_mu_var(n,p):
    return n * p, n * p * (1-p)

def geo(n,k,p=0.5):
    return (1-p)**(k-1) * p

def poisson(x,k):
    x**k * e**-x / factorial(k)

print(Stats.factorial(4))
# print(bernoulli(.5))
print(Stats.binomial_cdf(6,4, 0.9))
print(Stats.geo(6,0))

# cars going past intersection = x for y amt of time