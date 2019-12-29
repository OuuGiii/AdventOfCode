import os

from helper.file_helper import read_helper
dirname = os.path.dirname(__file__)
FILE_NAME = os.path.join(dirname, 'data.txt')


def main():
    list_of_numbers = read_helper.read_file_by_row_and_return_list_of_numbers(
        FILE_NAME)

    total_fuel_needed = calculate_total_fuel_needed(list_of_numbers)

    print("The total fuel needed is: {:d}".format(total_fuel_needed))


def calculate_total_fuel_needed(list_of_numbers):
    list_of_calculated_fuels = []

    for mass in list_of_numbers:
        fuel_needed = calculate_fuel_needed(mass)
        list_of_calculated_fuels.append(fuel_needed)

    total_fuel_needed = calculate_sum_of_list(list_of_calculated_fuels)

    return total_fuel_needed


# First divede by 3, then round down, then substract 2, keep continuing
def calculate_fuel_needed(mass):
    first_task = mass / 3
    second_task = int(first_task)
    third_task = second_task - 2
    fuel_needed = third_task

    if fuel_needed > 0:
        fuel_needed += calculate_fuel_needed(fuel_needed)
    else:
        fuel_needed = 0

    return fuel_needed


def calculate_sum_of_list(list_of_calculated_fuels):
    total_calculated_fuel = 0
    for calculated_fuel in list_of_calculated_fuels:
        total_calculated_fuel += calculated_fuel

    return total_calculated_fuel


main()
