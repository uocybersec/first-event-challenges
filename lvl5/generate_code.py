# this code is used for generating a new vault code. 
# you DO NOT need to understand this code to solve the challenge. 

from random import randint
from math import sqrt, floor

def isPrime(x): # returns True if 'x' is a prime number. Otherwise, returns False.
    for i in range(2, floor(sqrt(x))+1):
        if x % i == 0:
            return False
    return True

def generatePrime(*range): # generates a random prime number in a given range. Example: generatePrime(1, 50) generates a random prime number between 1 and 50 (inclusive). 
    while True:
        prime = randint(range[0], range[1])
        if isPrime(prime):
            return prime

key = generatePrime(1000, 9999)

code_length = randint(8, 16) # randomly decides how many numbers will compose the code 
code = []

for i in range(code_length):
    code.append(generatePrime(2,99) * key)

with open('encrypted_code.txt', mode='w') as code_file:
    code_file.write(' '.join([str(c) for c in code]))
