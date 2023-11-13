import math

# Trip planner

# 4.1 Bus stop information

bus_stop_dictionary = {
    1: [2, 1],
    2: [6, 1],
    3: [5, 3],
    4: [3, 4],
    5: [3, 6],
    6: [5, 7],
    7: [7, 6]
}


def print_dictionary(dictionary):
    for key in dictionary:
        bus_stop = dictionary[key]
        print(f"Location for bus stop {key} is {bus_stop}")


# print_dictionary(bus_stop_dictionary)

# 4.2


def find_euclidean_distance(loc1, loc2):
    x1 = loc1[0]
    y1 = loc1[1]
    x2 = loc2[0]
    y2 = loc2[1]

    return math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2))


def euclidean_distance_printer(stop_id_1, stop_id_2):
    loc1 = bus_stop_dictionary[stop_id_1]
    loc2 = bus_stop_dictionary[stop_id_2]
    euclidean_distance = find_euclidean_distance(loc1, loc2)
    print(f"The euclidean distance between bus stop {stop_id_1} and {stop_id_2} is {euclidean_distance}")


# euclidean_distance_printer(1, 3)


# 4.3
def euclidean_distances_to_dictionary(input_loc):
    distances = {}
    for key in bus_stop_dictionary:
        stop_loc = bus_stop_dictionary[key]
        distance = find_euclidean_distance(input_loc, stop_loc)
        distances[key] = distance
    return distances


def find_nearest_stops(input_loc):
    distances = euclidean_distances_to_dictionary(input_loc)
    stops = []
    counter = min(distances.values())

    for distance_key in distances:
        distance = distances[distance_key]
        if distance <= counter:
            stops.append(distance_key)
    return stops


def message_formatter(input_loc):
    stops = find_nearest_stops(input_loc)
    message = "The nearest "
    stops_length = len(stops)
    if stops_length == 1:
        message += "stop is Stop " + str(stops[0]) + "."
    elif stops_length > 1:
        loop_counter = 0
        for stop in stops:
            loop_counter += 1
            if loop_counter == 1:
                message += "stops are Stop: " + str(stop)
            elif loop_counter == stops_length:
                message += " and " + str(stop) + "."
            else:
                message += ", " + str(stop)
    return message


def print_nearest_stops():
    input_x = input("Enter your coordinate (x):")
    input_y = input("Enter your coordinate (y):")
    message = message_formatter([float(input_x), float(input_y)])
    print(message)


# print_nearest_stops()


# Optional (easier) version


def alternative_nearest_stop(input_loc):
    counter = 10000000
    nearest_stop = 0
    for key in bus_stop_dictionary:
        stop_loc = bus_stop_dictionary[key]
        distance = find_euclidean_distance(input_loc, stop_loc)
        if distance < counter:
            nearest_stop = key
            counter = distance
    return nearest_stop


def alternative_print_nearest_stop():
    input_x = input("Enter your coordinate (x):")
    input_y = input("Enter your coordinate (y):")
    nearest_stop = alternative_nearest_stop([float(input_x), float(input_y)])
    print(f"The nearest stop is Stop {nearest_stop}.")


# alternative_print_nearest_stop()
# 4.4


travel_time_dictionary = {
    1: find_euclidean_distance([2, 1], [6, 1]) * 2.5,
    2: find_euclidean_distance([6, 1], [5, 3]) * 2.5,
    3: find_euclidean_distance([5, 3], [3, 4]) * 4,
    4: find_euclidean_distance([3, 4], [3, 6]) * 4,
    5: find_euclidean_distance([3, 6], [5, 7]) * 4,
    6: find_euclidean_distance([5, 7], [7, 6]) * 2.5
}


def estimated_time(departure, destination):
    travel_time = 0
    bus_stops = list(range(departure, destination))
    for routes in travel_time_dictionary:
        for stops in bus_stops:
            if routes == stops:
                travel_time += travel_time_dictionary[routes]
    return travel_time


def print_estimated_time():
    departure = int(input("Departure stop:"))
    destination = int(input("Destination stop:"))
    travel_time = round(estimated_time(departure, destination), 1)
    print(f"Estimated bus travel time: {travel_time} min")


print_estimated_time()
