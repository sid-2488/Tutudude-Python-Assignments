# area of triangle

"""
when all the length of the sides of the triangle is known - a, b , c
semi perimeter (s) = a + b + c/2
Area = square root of (s * (s-a) * (s-b) * (s-c)
"""
a = float(input("Enter the side A: "))
b = float(input("Enter the side B: "))
c = float(input("Enter the side C: "))
s = (a + b + c) / 2
area = (s * (s-a) * (s-b) * (s-c)) ** 0.5
print("The area of the triangle of the given side is", round(area,2))

