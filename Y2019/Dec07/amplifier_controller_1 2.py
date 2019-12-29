import os
from helper.file_helper import read_helper
from helper.list_helper import list_helper

from helper.int_code_helper.int_code_v5 import IntCode

dirname = os.path.dirname(__file__)
FILE_NAME = os.path.join(dirname, 'data.txt')


def main():
    list_of_numbers = read_helper.read_file_and_split_by_character_and_return_list_of_numbers(
        FILE_NAME, ",")

    max_amplifier = find_max_amplifier(list_of_numbers)

    print("\nThe max amplifier is: {:d}".format(max_amplifier))


def find_max_amplifier(list_of_numbers):
    amplifiers = []

    A_second_input = 0

    for A in range(0, 5):
        for B in range(0, 5):
            if B == A:
                continue
            for C in range(0, 5):
                if C == A or C == B:
                    continue
                for D in range(0, 5):
                    if D == A or D == B or D == C:
                        continue
                    for E in range(0, 5):
                        if E == A or E == B or E == C or E == D:
                            continue
                        print(
                            "Running amplifier control for setting: [{}, {}, {}, {}, {}]"
                            .format(A, B, C, D, E))

                        ampA = IntCode(list_of_numbers.copy(), A, 0)
                        ampB = IntCode(list_of_numbers.copy(), B,
                                       ampA.last_output)
                        ampC = IntCode(list_of_numbers.copy(), C,
                                       ampB.last_output)
                        ampD = IntCode(list_of_numbers.copy(), D,
                                       ampC.last_output)
                        ampE = IntCode(list_of_numbers.copy(), E,
                                       ampD.last_output)

                        amplifiers.append(ampE.last_output)

    max_amplifier = list_helper.find_max_value_in_list(amplifiers)

    return max_amplifier


def get_phase_settings(number):
    list_of_digits = list(str(number))
    phase_settings = []

    number_of_leading_zeros = 5 - len(list_of_digits)

    for i in range(0, number_of_leading_zeros):
        phase_settings.append(0)

    for i in range(0, len(list_of_digits)):
        phase_settings.append(int(list_of_digits[i]))

    return phase_settings


main()
