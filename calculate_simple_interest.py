""""
simple interest = (p * r * t) / 100
p = principal amount
r = rate of interest
t = time duration in years
"""

principal = float(input("Enter principal amount: "))
rate = float(input("Enter interest rate: "))
time = float(input("Enter durattion in years: "))

si = (principal * rate * time) / 100
print("simple interset is", si)
