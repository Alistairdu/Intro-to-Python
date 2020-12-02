from numpy import var, mean, std

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


