# Task 1

first_name = input("Enter your first name:").lower()
initial = first_name[0]

second_name = input("Enter your second name:").lower()

name = ".".join([initial, second_name])

bi_mail = "@".join([name, "bi.no"])
print(f"Your mail is {bi_mail}")


# Task 2

diameter = input("Enter diameter:")

area = 3.14 * ((float(diameter)/2)**2)
print(f"The area of the circle is {area}.")


# Task 3


def coupon_finder(amount):
    if 300 <= amount < 500:
        return amount * 0.05
    elif 500 <= amount < 1000:
        return amount * 0.08
    elif 1000 <= amount:
        return amount * 0.1
    else:
        return 0


amount_spent = int(input("Please enter your purchase amount:"))
coupon = int(coupon_finder(amount_spent))
print(f"You get a coupon worth {coupon}.")


# Task 4

sales = [300, 250, 320, 240, 330, 320, 290, 280, 320, 270]
inventory = 3000
for sale in sales:
    inventory -= sale
    message = f"{inventory}"
    if inventory < 800:
        print(message + " (low inventory")
    else:
        print(message)


# Task 5
