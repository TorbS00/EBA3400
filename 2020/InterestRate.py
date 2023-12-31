# Interest Rate
# Simple Interest Equation: A=P(1+rt)
# Compound Interest Equation: A=P*(1+r/n)^(nt)

# Task A
# Create a function for simple interest rate equation

# Simple Interest Equation
# Calculates total accrued amount
# P = Principal amount
# r = Rate of interest per year in decimal
# t = Time period involved in months or years
def simple_interest(p, r, t):
    return p * (1 + r * t)


print("Task A")
a_accrued_amount = round(simple_interest(5000, 0.07, 5), 2)
print(f"Total accrued amount is ${a_accrued_amount}")
print()


# Task B
# Create a function for compound interest rate equation

# Compound Interest Equation
# Calculates total accrued amount
# P = Principal amount
# r = Rate of interest per year in decimal
# t = Time period involved in months or years
# n = number of compounding periods per unit t
def compound_interest(p, r, t, n):
    return p * ((1 + r / n) ** (t*n))


print("Task B")
b_accrued_amount = round(compound_interest(5000, 0.07, 5, 1), 2)
print(f"Total accrued amount is ${b_accrued_amount}")
print()


# Task C
# Use  the  function  in  part(a)  and  calculate  for  investing  an  original
# 1000  dollar  at  5%  simple annually, how much you have in total after 7 years
print("Task C")
c_accrued_amount = round(simple_interest(1000, 0.05, 7), 2)
print(f"Total accrued amount is ${c_accrued_amount}")
print()


# Task D
# Use the function in part(b) and calculate for investing an original
# 1000 dollar at 5% compounded annually, how much you have after 7 years
print("Task D")
d_accrued_amount = round(compound_interest(1000, 0.05, 7, 1), 2)
print(f"Total accrued amount is ${d_accrued_amount}")
print()


# Task E
# Use  the  function  in part(b)  and  calculate  for  investing an  original
# 2000  dollar  at  12% compounded monthly, how much you have after 5 years
print("Task E")
e_accrued_amount = round(compound_interest(2000, 0.12, 5, 12), 2)
print(f"Total accrued amount is ${e_accrued_amount}")
print()
