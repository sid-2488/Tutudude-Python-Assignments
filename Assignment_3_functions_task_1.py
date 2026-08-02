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
