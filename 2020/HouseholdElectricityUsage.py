# Task A)
# Create a function that returns price you pay per kilowatt-hour(kWh)
# of electricity in dollar for one day

# Cost function for one day in dollars
def cost_function(watt, hours, rate):
    return (((watt * hours) / 1000) * rate) / 100

# Testing the price usage of TV for one day.


price_day = cost_function(150, 5, 12)
print("\033[1m" + "Task A:" + "\033[0m")

print("Usage of TV for one day ($): " + str(price_day))
print()

# Task B)
# Use an iterative procedure (a loop) to determine the price
# for 1, 3,6, 12 months. Use information about calculation from part (a)
print("\033[1m" + "Task B:" + "\033[0m")

for month in (1, 3, 6, 12):
    price = price_day * month * 30
    message = "Price for {} month(s) is ${}"
    print(message.format(month, round(price, 2)))
print()

# Task C)
# What  is  the  price  of  three  different  electric  devices
# (TV,  computer,  refrigerator)  using  (150, 200,1000)
# watt using (5, 12,24) hours per day with a rate that you
# get as an input(eg.,12 cents)?Use your function from
# previous parts to answer the question.
print("\033[1m" + "Task C:" + "\033[0m")


def cost_from_rate(rate):

    items = [
        {"item": "TV", "watt": 150, "hours": 5},
        {"item": "computer", "watt": 200, "hours": 12},
        {"item": "refrigerator", "watt": 1000, "hours": 24}
    ]

    for item in items:
        price_item = cost_function(item["watt"], item["hours"], rate)
        name_item = item["item"]
        message = "Price for {} each day ${}"
        print(message.format(name_item, round(price_item, 2)))


cost_from_rate(12)




