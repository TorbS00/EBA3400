# Data dispersion measurement

def mean_of_list(number_list):
    size = len(number_list)
    counter = 0
    for number in number_list:
        counter += number
    return counter / size


def sum_of_list(number_list):
    mean = mean_of_list(number_list)
    counter = 0
    for number in number_list:
        x = abs(number - mean)
        counter += x
    return counter


def dispersion(number_list):
    size = len(number_list)
    summation = sum_of_list(number_list)
    return round(summation / size, 2)


list_1 = [4, 1, 4, 1, 3, 5]
list_2 = [43, 31, 41, 40, 40, 48, 29, 48, 23, 33]

dispersion_1 = dispersion(list_1)
dispersion_2 = dispersion(list_2)

print(f"(1) list_1 gives a dispersion of {dispersion_1}")
print(f"(2) list_2 gives a dispersion of {dispersion_2}")


