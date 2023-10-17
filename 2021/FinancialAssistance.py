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


# Function for checking if the input is an integer (whole number)
def input_integer_check(user_input):
    try:
        int(user_input)
        return True
    except ValueError:
        return False


print("\033[1m" + "Financial assistance calculator!" + "\033[0m")
input_income = input("Please enter your household income:")
while not input_integer_check(input_income):
    input_income = input("Your household needs to be an integer, try again:")
int_input_income = int(input_income)
print()


input_children = input("How many children do you have:")
while not input_integer_check(input_children):
    input_children = input("Your amount of children needs to be an integer, try again:")
int_input_children = int(input_children)
print()


financial_support = financial_assistance(int_input_income, int_input_children)
message = "The financial support for a household with ${} income and {} children is ${}"
print(message.format(input_income, input_children, financial_support))
