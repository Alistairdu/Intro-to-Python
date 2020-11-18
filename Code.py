from random import random
from math import e

def factorial(n):
    prod = 1
    for num in range(1,n+1):
        prod *= num
    return prod

def permutation(n,k):
    return int(factorial(n) / factorial(n-k))

def choose(n,k):
    # return int(factorial(n) / (factorial(n-k) * factorial(k)))
    return int(permutation(n,k) / factorial(k))

def bernoulli(p):
    if random()<p:
        return 1
    return 0

def binomial(n,k,p=0.1):
    return choose(n,k) * p**k * (1-p)**(n-k)

def binomial_cdf(n,k,p):
    out = 0
    for i in range(n+1):
        out += binomial(n,i,p)
    return out

print(choose(5,2))
# print(binomial_cdf(15,4,0.7))


























# def binomial(n,p, k):
#     return (choose(n,k) * p**k * (1-p)**(n-k))

# def bin_cdf(n,p,k):
#     # prob = 0
#     # for i in range(k+1):
#     #     prob += binomial(n,p,i)
#     # return prob
#     return sum([binomial(n, p, i) for i in range(k +1)])

# print(bin_cdf(n = 12,k = 6, p = 0.5, ))

# def bin_cdf(n,k,p=0.5):
#     prob = 0
#     for i in range(k+1):
#         prob += binomial(n, i, p)
#     return prob

# # print(bernoulli(0.25))

# num_succ = sum([1 for _ in range(10) if bernoulli(.5)])

# # print(num_succ)

# # Import the plotting module
# from matplotlib import pyplot as plt

# # Set the seed for reproducability
# random.seed(152)
# # Declare an empty list to capture the results from each
# # binomial experiment
# result_lst = []

# # Execute 100,000 binomial experiments
# for _ in range(100000):
#     result_lst.append(sum([1 for _ in range(20) if bernoulli(.5)]))

# # # Plot the histogram
# plt.hist(result_lst, bins = 17)
# plt.show()


# # Define n, p, and size
# n, p, size = 20, .5, 10000

# # Set the seed
# random.seed(152)

# # # Create the plot
# # plt.hist(random.binomial(n, p, size), bins = 20)
# # plt.show()

# # print(bin_cdf(n = 139, p = 0.2, k = 25) - bin_cdf(n = 139, p = 0.2, k = 9))

# # Import the module
# from scipy.stats import binom
# from numpy import random

# # Set the random seed
# random.seed(123)

# # Use the
# mean, var, skew, kurt = binom.stats(139, 0.2, moments='mvsk')

# # print(f'Mean: {mean:.2f}, Variance: {var:.2f}, ' +
# #       f'Skewness: {skew:.2f}, Kurtosis: {kurt:.4f}')



# print(binom.pmf(k = 15, n = 139, p = 0.02))
# prob = binom.cdf(k = 25, n = 139, p = 0.2) - binom.cdf(k = 9, n = 139, p = 0.2)

# # Print the probability
# print(prob)

# def geo(p, k):
#     return (1-p)**(k-1) * p

# from math import sqrt

# def geo_cdf(p,k):
#     prob = 0
#     for i in range(1,k+1):
#         prob += geo(p,i)
#     return prob

# def geo_cdf2(p,k):
#     return 1-(1-p)**k
# # print(geo_cdf(1/6, 4))
# # print(geo_cdf2(0.00016, 2000))

# def geo_mu_std(p):
#     return 1/p, sqrt((1-p)/p**2)

# def poisson(lam,k):
#     return lam**k * e**-lam / factorial(k)

# def poisson_cdf(lam,k): # for prob outcome > k
#     prob = 0
#     for i in range(k+1):
#         prob += poisson(lam,i)
#     return prob

# def poisson_pmf_dict(lam, highk, lowk):
#     d = {}
#     for i in range(lowk, highk+1):
#         d[i] = poisson(lam,i)
#     return d

# def poisson_cdf_dict(lam, highk, lowk):
#     d = {}
#     for i in range(lowk, highk+1):
#         d[i] = round(poisson_cdf(lam,i),3)
#     return d

# lam = 7
# highk = 19
# lowk = 0
# print(poisson_cdf_dict(lam, highk, lowk))

# # print(1/0.00016)




