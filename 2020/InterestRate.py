# Interest Rate
# Simple Interest Equation: A=P(1+rt)
# Compound Interest Equation: A=P*(1+r/n)^(nt)

# Task A
# Create a function for simple interest rate equation

# Simple Interest Equation
# Calculates total accrued amount
# P = Principal amount
# R = Rate of interest per year in decimal
# T = Time period involved in months or years
def simple_interest(p, r, t):
    return p * (1 + r * t)


print("\033[1m" + "Task A:" + "\033[0m")
accrued_amount = round(simple_interest(5000, 0.07, 5), 2)
message = "Total accrued amount is ${}"
print(message.format(accrued_amount))
print()

