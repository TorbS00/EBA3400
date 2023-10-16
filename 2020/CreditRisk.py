# Task A)
# Create a function to calculate Expected loss

# Converts percentage to decimal
def percentage_converter(percentage):
    return percentage / 100


# EAD = Exposure at default in dollar
# PD  = Probability of default in percent
# LGD = Loss given default in percent
# Returns expected loss in dollar
def expected_loss(ead, pd, lgd):
    return percentage_converter(pd) * ead * (1 - percentage_converter(lgd))


print("\033[1m" + "Task A:" + "\033[0m")
print("Calculated expected loss for the company is: $" +
      str(round(expected_loss(1000000, 100, 55), 2)))
print()

# Task B)
# Put the given table (customerID, Loan amount, PD, EAD, LGD) in the list
print("\033[1m" + "Task B:" + "\033[0m")
customers = [
    {"CustomerID": "A20001", "PD": 1, "EAD": 10000, "LGD": 10},
    {"CustomerID": "A20002", "PD": 2, "EAD": 20000, "LGD": 20},
    {"CustomerID": "A20003", "PD": 3, "EAD": 30000, "LGD": 30},
    {"CustomerID": "A20004", "PD": 4, "EAD": 40000, "LGD": 40},
    {"CustomerID": "A20005", "PD": 5, "EAD": 50000, "LGD": 50}
]
print("Customer list:")
for customer in customers:
    print(customer)
print()


#Task C)
# Create  a  function  to  read  the  given  list  from  part  (b)
# and  calculate  Expected  loss  for  each customerID and print the result
print("\033[1m" + "Task C:" + "\033[0m")
print("Expected loss for customers:")
for customer in customers:
    id = customer["CustomerID"]
    pd = customer["PD"]
    ead = customer["EAD"]
    lgd = customer["LGD"]
    customer_loss = round(expected_loss(ead, pd, lgd), 2)
    message = "Expected loss for customer {} is ${}"
    print(message.format(id, customer_loss))


