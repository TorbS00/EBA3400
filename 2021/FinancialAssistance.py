# Financial assistance
# The function used to calculate financial support
def financial_assistance(income, children):
    if 30000 <= income <= 40000:
        if children >= 3:
            return 1000 * children
    elif 20000 <= income <= 30000:
        if children >= 2:
            return 1500 * children
    elif income < 20000:
        return 2000 * children
    return 0


# Function used to checking and returning user input as integer
def convert_input(input_message):
    while not(user_input:=input(input_message)).isdecimal():
        print("Your input must be an integer...")
    print()
    return int(user_input)


print("\033[1mFinancial assistance calculator!\033[0m")
print()

income = convert_input("What is your household income:")
children = convert_input("How many children do you have:")
financial_support = financial_assistance(income, children)

print(f"The financial support for a household with ${income} "
      f"income and {children} children is ${financial_support}")

