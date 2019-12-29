import os
from helper.file_helper import read_helper
from helper.list_helper import list_helper

from helper.int_code_helper.int_code_v6 import IntCode

dirname = os.path.dirname(__file__)
FILE_NAME = os.path.join(dirname, 'data.txt')


def main():
    list_of_numbers = read_helper.read_file_and_split_by_character_and_return_list_of_numbers(
        FILE_NAME, ",")

    max_amplifier = find_max_amplifier(list_of_numbers)

    print("\nThe max amplifier is: {:d}".format(max_amplifier))


def find_max_amplifier(list_of_numbers):
    amplifiers = []

    for A in range(5, 10):
        for B in range(5, 10):
            if B == A:
                continue
            for C in range(5, 10):
                if C == A or C == B:
                    continue
                for D in range(5, 10):
                    if D == A or D == B or D == C:
                        continue
                    for E in range(5, 10):
                        if E == A or E == B or E == C or E == D:
                            continue

                        amplifier = get_amplifier_for_phase_setting(
                            A, B, C, D, E, list_of_numbers)

                        amplifiers.append(amplifier)

    max_amplifier = list_helper.find_max_value_in_list(amplifiers)

    return max_amplifier


def get_amplifier_for_phase_setting(A, B, C, D, E, list_of_numbers):
    amplifier = None

    print("Running amplifier control for setting: [{}, {}, {}, {}, {}]".format(
        A, B, C, D, E))

    ampA = IntCode(list_of_numbers.copy())
    ampB = IntCode(list_of_numbers.copy())
    ampC = IntCode(list_of_numbers.copy())
    ampD = IntCode(list_of_numbers.copy())
    ampE = IntCode(list_of_numbers.copy())

    ampA.inputs.append(A)
    ampB.inputs.append(B)
    ampC.inputs.append(C)
    ampD.inputs.append(D)
    ampE.inputs.append(E)

    ampA.inputs.append(0)

    while not ampE.has_ended:

        if not ampA.has_ended:
            #print("Running ampA")
            print("ampA inputs: {}".format(ampA.inputs))
            ampA.run_automatic_intCode()
            ampB.inputs.append(ampA.last_output)
        if not ampB.has_ended:
            #print("Running ampB")
            print("ampB inputs: {}".format(ampB.inputs))
            ampB.run_automatic_intCode()
            ampC.inputs.append(ampB.last_output)
        if not ampC.has_ended:
            #print("Running ampC")
            print("ampC inputs: {}".format(ampC.inputs))
            ampC.run_automatic_intCode()
            ampD.inputs.append(ampC.last_output)
        if not ampD.has_ended:
            #print("Running ampD")
            print("ampD inputs: {}".format(ampD.inputs))
            ampD.run_automatic_intCode()
            ampE.inputs.append(ampD.last_output)
        if not ampE.has_ended:
            #print("Running ampE")
            print("ampE inputs: {}".format(ampE.inputs))
            # print("ampE current position: {}".format(ampE.current_position))
            # print("ampE length of list: {}".format(len(ampE.list_of_numbers)))
            # print("ampE has ended: {}".format(ampE.has_ended))
            # print("ampE numbers left: {}".format(ampE.list_of_numbers[518:]))

            # if (ampE.current_position == 518):
            #     break
            ampE.run_automatic_intCode()
            ampA.inputs.append(ampE.last_output)
            #print("ampE inputs: {}".format(ampE.inputs))

    amplifier = ampE.last_output

    return amplifier


# This is not used,
# but I used it in the beginning to just put in a number
# and you will get a 5 digit phase setting of that number
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
