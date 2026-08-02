"""
Problem Statement: Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.

"""


# Create the file and write the initial content

with open("output.txt", "w") as fh:
    fh.write("Hello Python\n")

# Ask the user to enter additional text

user_input = input("Please enter a statement : ")

# Append the user's input to the file

with open("output.txt", "a") as fh:
    fh.write(user_input)

    # Open the file and read all lines
try:
    with open("output.txt", "r") as fh:
        data = fh.readlines()

except FileNotFoundError:
    print("File not found")

else:
    for line in data:
        print(line.rstrip())

finally:
    print("Assignment 4 completed")


