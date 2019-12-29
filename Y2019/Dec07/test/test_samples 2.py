import os
from helper.file_helper import read_helper
from helper.list_helper import list_helper

from helper.int_code_helper.int_code_v6 import IntCode

dirname = os.path.dirname(__file__)
FILE_NAME = os.path.join(dirname, 'data.txt')


def main():
    list_of_numbers = read_helper.read_file_and_split_by_character_and_return_list_of_numbers(
        FILE_NAME, ",")

    amplifier = get_amplifier_for_phase_setting(9, 7, 8, 5, 6, list_of_numbers)

    print("\nThe max amplifier is: {:d}".format(amplifier))


def get_amplifier_for_phase_setting(A, B, C, D, E, list_of_numbers):
    amplifier = None

    ampA = IntCode(list_of_numbers.copy())
    ampB = IntCode(list_of_numbers.copy())
    ampC = IntCode(list_of_numbers.copy())
    ampD = IntCode(list_of_numbers.copy())
    ampE = IntCode(list_of_numbers.copy())

    print("Running amplifier control for setting: [{}, {}, {}, {}, {}]".format(
        A, B, C, D, E))

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
            ampE.run_automatic_intCode()
            ampA.inputs.append(ampE.last_output)
            #print("ampE inputs: {}".format(ampE.inputs))

    amplifier = ampE.last_output

    return amplifier


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