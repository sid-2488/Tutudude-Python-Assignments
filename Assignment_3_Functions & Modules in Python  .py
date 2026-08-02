# Task 1: Calculate Factorial Using a Function

# Ask the user to enter a number
num = int(input("Enter a number: "))

# Define a recursive function to calculate the factorial
def factorial(n):
    if n == 0:
        return 1 # base case
    else:
        return n * factorial(n - 1)  # Recursive case: Multiply the number by the factorial of the previous number

# Display the factorial of the entered number
print(f"The factorial of {num} is : {factorial(num)}")

# Task 2: Using the Math Module for Calculations

import math # first step we need to import the math module

# Ask the user to enter a number
num1 = int(input("Enter a number: "))

def square_root(n):
    if n == 0:
        return 0 # base case
    else:
        return math.sqrt(n) # Return the square root of the entered number

print(f"The square root of {num1} is : {square_root(num1)}")

def logarithmic(n):
    if n == 0:
        return 0 # base case
    else:
        return math.log(n)  # Return the natural logarithm (base e) of the entered number

print(f"The (log base e of the {num1}) is : {logarithmic(num1)}")


def sine(n):
    if n == 0:
        return 0 # base case
    else:
        return math.sin(n) # # Return the sine of the entered number


print(f"The sine of the {num1} is : {sine(num1)}")

