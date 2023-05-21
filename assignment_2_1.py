'''
Assignment_2_1: Finding 450th prime number
May 21, 2023
Sai Himalay Nikhil, Kondapally

'''
primeCount = 1
num = 1

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


while primeCount<450:
    num+= 2
    if primeCheck(num):
        primeCount += 1
        if primeCount % 50 ==0:
            print(f"{primeCount} prime numbers found so far.\n")
    


print(f"This program is aimed to find the 450th prime number and the answer is: {num}\n")