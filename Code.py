from math import e
from random import random

def factorial(n):
    prod = 1
    for i in range(2,n+1):
        prod *= i
    return prod

def permutation(n,k):
    return int(factorial(n) / factorial(n-k))

def choose(n,k):
    return int(permutation(n,k) / factorial(k))

def bernoulli(p):
    if random() < p:
        return 1
    return 0

def binomial(n,k,p=0.5):
    return choose(n,k) * p**k * (1-p)**(n-k)

def bin_cdf(n,k,p=0.5):
    return sum([binomial(n,i,p) for i in range(k+1)])

def bin_mv(n,p=0.5):
    return n * p, n * p * (n-p)

def geo(n,k,p=0.5): # first success is on kth trial
    return (1-p)*(k-1) * p

print(geo(10,1,0.5))
print(0.5**0)

def geo_cdf(n,k,p=0.5):
    return sum([geo(n,i,p) for i in range(1,k+1)])

def geo_cdf1(n,k,p=0.5):
    return 1-((1-p)**k)

'''
def geometric_cdf(p, k, inclusive=True):
    acc = 0 
    if inclusive: 
        low_k = 1
    else: 
        low_k = 0        
    for value in range(low_k, k+1) : 
        acc += geometric_pmf(p, value, inclusive)
    return acc 
print(geometric_cdf(0.5, 7, inclusive=True)) #0.9921875

Geometric Distribtuion:
    like the Binomial Dist., Geometric models a sequence of Bernoulli trials. 
     - however, where Binomial models k success in n trials
        Geometric models how many trials till the first success  
            where k = # of trials up to and including first success
            (or k = # failrues before 1st success - uncommon interpretation)
    Geo PMF = X ~ geometric(p), or X ~ G(p) 
        P(X = k) = (1-p)**(k-1) * p   for 1<= k <= infinity
            k = trial where fist success encountered
    Expected value = mu = 1/p
    Var(X) = (1-p) / p**2

    Geo CDF = has formula not needing summation
        P(X<=k) = 1-(1-p)**k    for 1<= k <= infinity
            -> think of as first success is > k = prior buckets failed:
                (1-p)**k 
            complement of this = prob success is on or before k = 1-(1-p)**k
'''


# print(factorial(5))
# print(choose(5,2))
# print(bernoulli(0.7))
# print(binomial(10,10,0.9))
# print(bin_cdf(10,9,0.9))
# print(bin_mv(10,0.9))
# print(geo_cdf(10,2,0.9))
# print(geo_cdf1(10,2,0.9))
# print(geo_mv(10,2,0.9))