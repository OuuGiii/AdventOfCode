import os

dirname = os.path.dirname(__file__)
FILE_NAME = os.path.join(dirname, 'data.txt')


def main():
    list_of_numbers = read_file_and_return_list_of_numbers(FILE_NAME)

    total_fuel_needed = calculate_total_fuel_needed(list_of_numbers)

    print("The total fuel needed is: {:d}".format(total_fuel_needed))


def read_file_and_return_list_of_numbers(file_name):
    list_of_numbers = []
    with open(file_name, "r") as file:
        for line in file:
            number = int(line)
            list_of_numbers.append(number)

    return list_of_numbers


def calculate_total_fuel_needed(list_of_numbers):
    list_of_calculated_fuels = []

    for mass in list_of_numbers:
        fuel_needed = calculate_fuel_needed(mass)
        list_of_calculated_fuels.append(fuel_needed)

    total_fuel_needed = calculate_sum_of_list(list_of_calculated_fuels)

    return total_fuel_needed


# First divede by 3, then round down, then substract 2
def calculate_fuel_needed(mass):
    first_task = mass / 3
    second_task = int(first_task)
    third_task = second_task - 2

    fuel_needed = third_task

    return fuel_needed


def calculate_sum_of_list(list_of_calculated_fuels):
    total_calculated_fuel = 0
    for calculated_fuel in list_of_calculated_fuels:
        total_calculated_fuel += calculated_fuel

    return total_calculated_fuel


main()
