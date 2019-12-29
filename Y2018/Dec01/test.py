import os
from collections import Counter
dirname = os.path.dirname(__file__)
FILE_NAME = os.path.join(dirname, 'data1.txt')


def main():
    list_of_numbers = [+1, -1]

    first_frequency_reached_twice = find_first_frequency_reached_twice(
        list_of_numbers)
    print("the first frequency reached twice is: {:d}".format(
        first_frequency_reached_twice))


def read_file_and_return_list_of_numbers(file_name):
    list_of_numbers = []
    with open(file_name, "r") as file:
        for line in file:
            number = int(line)
            list_of_numbers.append(number)

    return list_of_numbers


def find_first_frequency_reached_twice(list_of_numbers):
    sums = [0]
    sum = 0

    times = 0

    while (times < 100):

        for number in list_of_numbers:
            sum += number

            if sum in sums:
                return sum

            sums.append(sum)

        times += 1


def find_first_item_repeated_in_list(a_list):
    for item1 in a_list:
        x = 0
        for item2 in a_list:
            if item1 == item2:
                x += 1
        if x > 1:
            return item1


main()
