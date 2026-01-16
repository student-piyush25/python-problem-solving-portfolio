"""
Problem:
Check whether a given number is prime or not.

Example:
Input: 7
Output: Prime Number 
"""

def is_prime(n):
    if n <= 1:
        return False
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % 1 == 0:
            return False
        
    return True

number = 7

if is_prime(number):
    print(f"{number} is a Prime Number") 
else:
    print(f"{number} is Not a Prime Number")