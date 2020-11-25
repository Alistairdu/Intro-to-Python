# Invent problems for all kinds of stats we have available and solve them
from math import e, factorial
from scipy.stats import poisson

def choose(n,k):
    return factorial(n)/(factorial(n-k) * factorial(k))

def binomial(n,k,p):
    return choose(n,k) * p**k * (1-p)**(n-k)

def geo(k,p): # first success is on kth trial
    return (1-p)**(k-1) * p

def geo_cdf(k,p):
    return sum([geo(i,p) for i in range(1,k+1)])

def geo_cdff(k,p):
    return 1-(1-p)**k

def poisson(lamb,k):
    return lamb**k * e**-lamb / factorial(k)

def poisson_cdf(lamb,k):
    return sum([poisson(lamb,i) for i in range(k+1)])

def poisson_mv(lam):
    return lam, lam

lamb = 5
n = 10
k = 5
p = 0.5

# First, import the necessary function from the scipy.stats package
from scipy.stats import norm

# Call the norm function to make the calculation
print(norm.cdf(53, loc=46, scale=1.75))
print(norm.cdf(3.54285714286))


# print(binomial(n,k,p))
# print(poisson(lamb,k))


# def geo_mv(p):
#     return 1/p, (1-p)/p**2
'''
you are riding you bike downtown. In any 10 blocks, 
you realize that you have on average 2 blocks w police cars.
What is the probability that you see 7 blocks w police cars in the next 10 blocks?




'''
