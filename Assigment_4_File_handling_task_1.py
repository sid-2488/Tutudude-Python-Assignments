"""Task 1: Read a File and Handle Errors
Problem Statement:  Write a Python program that:
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist.
"""


with open("sample.txt", "w") as fh: # use the w mode to create a file if does not exist
    fh.write("Line 1 : This is a sample text file \n")
    fh.write("Line 2 : It contains multiple lines \n")

try:
    with open("sample.txt", "r") as fh:
        content = fh.readlines()

except FileNotFoundError:
        print("Error : The file sample.txt was not found")
else:
     for line in content:
         print(line.rstrip())

finally:
        print("Program completed")

