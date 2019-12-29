import os
from helper.file_helper import read_helper

dirname = os.path.dirname(__file__)
FILE_NAME = os.path.join(dirname, 'data.txt')


def main():
    list_of_numbers = read_helper.read_file_and_split_by_character_and_return_list_of_numbers(
        FILE_NAME, ",")

    noun, verb = find_noun_and_verb(list_of_numbers)
    value_at_position_0 = run_int_code_for_list_of_numbers(list_of_numbers)

    print("The Noun is: {:d}\nThe Verb is: {:d}".format(noun, verb))

    answer = 100 * noun + verb

    print("Answer is: 100 * {:d} + {:d} = {:d}".format(noun, verb, answer))


def setup_list(list_of_numbers, int1, int2):
    list_of_numbers[1] = int1
    list_of_numbers[2] = int2


def find_noun_and_verb(list_of_numbers):
    for noun in range(0, 100):
        for verb in range(0, 100):
            copy_list_of_numbers = list_of_numbers.copy()
            setup_list(copy_list_of_numbers, noun, verb)

            value_at_position_0 = run_int_code_for_list_of_numbers(
                copy_list_of_numbers)

            if (value_at_position_0 == 19690720):
                return noun, verb


def run_int_code_for_list_of_numbers(list_of_numbers):
    i = 0
    while i < len(list_of_numbers) - 1:
        if list_of_numbers[i] == 1:
            opCode1(i, list_of_numbers)
            i += 4

        elif list_of_numbers[i] == 2:
            opCode2(i, list_of_numbers)
            i += 4

        elif list_of_numbers[i] == 99:
            break

        else:
            i += 1

    return list_of_numbers[0]


# Opcode 1 adds together numbers read from two positions
# and stores the result in a third position.
# The three integers immediately after the opcode tell you these three positions -
# the first two indicate the positions from which you should read the input values,
# and the third indicates the position at which the output should be stored.
def opCode1(i, list_of_numbers):
    i1 = list_of_numbers[i + 1]
    i2 = list_of_numbers[i + 2]
    i3 = list_of_numbers[i + 3]

    list_of_numbers[i3] = list_of_numbers[i1] + list_of_numbers[i2]


# Opcode 2 multiply together numbers read from two positions
# and stores the result in a third position.
# The three integers immediately after the opcode tell you these three positions -
# the first two indicate the positions from which you should read the input values,
# and the third indicates the position at which the output should be stored.
def opCode2(i, list_of_numbers):
    i1 = list_of_numbers[i + 1]
    i2 = list_of_numbers[i + 2]
    i3 = list_of_numbers[i + 3]

    list_of_numbers[i3] = list_of_numbers[i1] * list_of_numbers[i2]


main()
