# Knapsack problem

# Task A
items = [
    {"name": "A", "weight": 5, "value": 310},
    {"name": "B", "weight": 3, "value": 270},
    {"name": "C", "weight": 4.5, "value": 220},
    {"name": "D", "weight": 1, "value": 150},
    {"name": "E", "weight": 3.5, "value": 140},
    {"name": "F", "weight": 2.5, "value": 90},
    {"name": "G", "weight": 4, "value": 70},
    {"name": "H", "weight": 3, "value": 60},
    {"name": "I", "weight": 2, "value": 50},
    {"name": "J", "weight": 1, "value": 30}
]

# Task B


def luggage_combination(max_weight):
    weight_counter = 0
    luggage = []
    for item in items:
        weight = item["weight"]
        if (weight_counter + weight) > max_weight:
            continue
        weight_counter += weight
        luggage.append(item)
    return luggage


# Testing the luggage combination
print(luggage_combination(23))
