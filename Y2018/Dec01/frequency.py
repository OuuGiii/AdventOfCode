import os
dirname = os.path.dirname(__file__)
FILE_NAME = os.path.join(dirname, 'data1.txt')


def main():
    list_of_numbers = read_file_and_return_list_of_numbers(FILE_NAME)

    sum = get_sum_of_list(list_of_numbers)
    print("resulting frequency: {:d}".format(sum))


def read_file_and_return_list_of_numbers(file_name):
    list_of_numbers = []
    with open(file_name, "r") as file:
        for line in file:
            number = int(line)
            list_of_numbers.append(number)

    return list_of_numbers


def get_sum_of_list(list_of_numbers):
    sum = 0
    for number in list_of_numbers:
        print(number)
        sum += number

    return sum


main()
