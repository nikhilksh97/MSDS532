'''
Assignment_2_2: Python progarm to demonstrate the sum of logarithms of primes 
between 2 and n will converge on the value of n.
May 21, 2023
Sai Himalay Nikhil, Kondapally

'''
from math import *

n_List = [50, 500,5000,50000]
i=1
num=1
lst = [log(2)]


def primeCheck(x):
    if x<=1:
        return False
    if x==2:
        return True
    if x%2==0:
        return False
    for i in range(3, int(x**0.5)+1, 2):
        if x%i == 0:
            return False
    return True

for n in n_List:
    if primeCheck(n):
        while i<=n:
            i+=2
            if primeCheck(i):
                lst.append(log(i))
    else:
        while i<=n:
            i+=2
            if primeCheck(i):
                lst.append(log(i))
    s = round(sum(lst))
    ratio = s/n
    print(f"n is: {n}")
    print(f"Sum is: {s}")
    print(f"Ratio is: {ratio}\n")







