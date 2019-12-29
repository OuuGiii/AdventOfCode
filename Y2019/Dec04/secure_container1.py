import os
from collections import defaultdict
from helper.file_helper import read_helper
from helper.list_helper import list_helper

# Puzzle input: 108457-562041
min_password = 108457
max_password = 562041


def main():

    possible_passwords = get_possible_passwords(min_password, max_password)

    number_of_possible_passwords = len(possible_passwords)

    print("The number of possible passwords is: {:d}".format(
        number_of_possible_passwords))


def get_possible_passwords(min_password, max_password):
    possible_passwords = []

    for password in range(min_password, max_password + 1):

        if (is_six_digit_number(password)
                and is_in_range(password, min_password, max_password)
                and two_adjacent_digits_are_the_same(password)
                and digits_never_decrease(password)):
            possible_passwords.append(password)

    return possible_passwords


def is_six_digit_number(password):
    if len(str(password)) == 6:
        return True
    return False


def is_in_range(password, min_password, max_password):
    if (min_password <= password <= max_password):
        return True
    return False


def two_adjacent_digits_are_the_same(password):
    current_number = None
    previous_number = None
    for i in str(password):
        current_number = int(i)

        if previous_number:
            if current_number == previous_number:
                return True

        previous_number = current_number

    return False


def digits_never_decrease(password):
    current_number = None
    previous_number = None
    for i in str(password):
        current_number = int(i)

        if previous_number:
            if current_number < previous_number:
                return False

        previous_number = current_number

    return True


main()
