"""
amount = p(1 + r/100) ** t
ci = amount - p
"""

principal = float(input("Enter principal amount: "))
rate = float(input("Enter interest rate: "))
time = float(input("Enter durattion in years: "))

#amount1 = principal  * (1 + rate/100) ** time
amount2 = principal  * pow((1 + rate/100),time)

print(round(amount2,2))
ci = amount2 - principal

print("The compund interest is", round(ci,2))





