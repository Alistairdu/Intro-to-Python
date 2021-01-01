'''from numpy import var, mean, std

def mean_(lst):
    return sum(lst) / len(lst)

def var_(lst,ddof):
    diffs = []
    for num in lst:
        diffs.append(num - mean(lst))
    squares = []
    for num in diffs:
        squares.append(num**2)
    return sum(squares)/(len(squares)-ddof)

def std_(lst,ddof):
    return var_(lst,ddof)**(1/2)

#calls - 

lst = [27,41,23,56,76,54,53,49,50,92,47,23,56,65,71,73,76,77,]
ddof = 1

print(mean_(lst)) # will give the mean of the list
print(mean(lst)) # will give the mean of the list
print(var_(lst,ddof)) # will give the variance of the list
print(var(lst,ddof=1)) # will give the variance of the list
print(std_(lst,ddof)) # will give the square root of the list
print(std(lst,ddof=1)) # will give the square root of the list



def factorial(n):
    prod = 1
    for i in range(2,n+1):
        prod *= i
    return prod

def choose(n,k):
    return int(factorial(n) / (factorial(k) * factorial(n-k)))

#call ->
n = 18
k = 5

print(factorial(n)) # 6 -> 720
print(choose(n,k)) # 6,1 -> 120

from collections import defaultdict
import random

count_dict = defaultdict(int)
for i in range(10):
  roll = random.randint(1, 6)
  count_dict[roll] += 1
print(count_dict)

from collections import defaultdict
some_dict = defaultdict(str)
print(some_dict['some_key'])

while True: # note, infinite loop
    input = input('Do you want to continue looking at this message? Spell the word "commitment" correctly in order to exit, otherwise we\'re doing this forever... ')

    if input == 'commitment':
        break'''
daily_temps = [61.2, 59.0, 59.4, 58.9, 60.1, 55.3, 55.6]

from numpy import mean

m = sum(daily_temps)/len(daily_temps)

print(mean(daily_temps), m)