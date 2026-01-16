"""
Problem:
Generate Fibonacci series up to n terms using:
1. Loop
2. Recursion

Example:
Input: 7
Output: 
"""

# ---------------------------------
# Method 1: Using Loop
# ---------------------------------

def fibonacci_loop(n):
    a, b = 0, 1
    
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
        
# ---------------------------------
# Mehtod 2: Using Recursion
# ---------------------------------
def fibonacci_recursive(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# test the function
terms = 7

print("Fibonacci using loop:")
fibonacci_loop(terms)

print("\n\nFibonacci using recursion:")
for i in range(terms):
    print(fibonacci_recursive(i), end=" ")