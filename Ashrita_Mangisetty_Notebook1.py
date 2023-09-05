#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math #this package is imported to perform math calculations

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True




# In[2]:


"""The above mentioned function initially checks for the special cases i.e., for n being less than or equal to 1, this returns False because prime numbers must be greater than 1. Further, it enters into a loop which iterates from 2 to square root of n.This loop checks if any number in this range divides n  without a remainderIf it finds any number that divides n evenly, it returns False because it has found a divisor, and n is not prime.If the loop completes without finding any divisors, it means that n is not divisible by any numbers in the range from 2 to the square root of n. In this case, it returns True, indicating that n is prime."""
 


# In[3]:


count = 0
primes = []    #this is a list to store all the prime numbers from 9991th to 10000th count

number = 2  #initialising as 2 because prime numbers starts from 2
while True : #loop runs and checks to find the prime numbers in the specified range below
    if isPrime(number):   #this checks if its prime or not by calling function isPrime
        count += 1
        if count >= 9991:  #if the count is greater than 9991 it appends the prime number in the list
            primes.append(number) 
        if count == 10000:  #the loop stops when we find 10000th prime number 
            break 
    number += 1   # number increment to check the prime by looping 
    continue  # Uses continue to skip non-prime numbers


for i, prime in enumerate(primes, 9991):  #this loop uses enumerate keyword to print all the numbers in primes list starting from 9991 position
    print(prime)   #this prints prime numbers along with with the position number between 9991 to 10000

with open('prime.txt', 'w') as file:   #this command is used to open a file with write permission
    for prime in primes:               #loop runs to write all the prime numbers in the list into the text file
        file.write(str(prime) + '\n')   




#1. Break: When count reaches 10000 (i.e., the 10000th prime is found), the break statement is used to comes out of the while loop,improving efficiency by stopping the search once the desired range is reached.
#2. Continue : This statement is used skip the numbers that are not prime, which can improve efficiency.

