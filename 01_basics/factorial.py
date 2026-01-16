"""
Problem:
Find the factorial of a given number using:
1. Recursion
2. Loop (Iterative method)

Example:
input-5
output: 120
"""

# -------------------------------
# Method 1: Using Recursion
# -------------------------------
def factorial_recursive(n):
    # base case
    if n==0 or n==1:
        return 1
    
    return n * factorial_recursive(n-1)

# -------------------------------
# Method 2: Using Loop
# -------------------------------
def factorial_loop(n):
    result = 1
    
    for i in range(1, n+1):
        result = result * i
        
    return result

# Testing both methods
number = 5

print("Using Recursion:", factorial_recursive(number))
print("Using Loop:", factorial_loop(number))

