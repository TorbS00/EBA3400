# Financial assistance
# The function used to calculate financial support
def financial_assistance(input_income, input_children):
    if 30000 <= input_income <= 40000:
        if input_children >= 3:
            return 1000 * input_children
    elif 20000 <= input_income <= 30000:
        if input_children >= 2:
            return 1500 * input_children
    elif input_income < 20000:
        return 2000 * input_children
    return 0


# Function used to checking and returning user input as integer
def convert_input(input_message):
    while not(user_input := input(input_message)).isdecimal():
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

