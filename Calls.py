from Code import var_, mean_, std_

#calls - 58423578

lst = [27,41,23,56,76,54,53,49,50,92,47,23,56,65,71,73,76,77,]
ddof = 1

print(mean_(lst)) # will give the mean of the list
# print(mean(lst)) # will give the mean of the list
print(var_(lst,ddof)) # will give the variance of the list
# print(var(lst,ddof=1)) # will give the variance of the list
print(std_(lst,ddof)) # will give the square root of the list
# print(std(lst,ddof=1)) # will give the square root of the list