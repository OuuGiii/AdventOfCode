import os
from helper.file_helper import read_helper

dirname = os.path.dirname(__file__)
FILE_NAME = os.path.join(dirname, 'data.txt')


def main():
    list_of_numbers = read_helper.read_file_and_split_by_character_and_return_list_of_numbers(
        FILE_NAME, ",")

    setup_list_correctly(list_of_numbers)

    value_at_position_0 = run_int_code_for_list_of_numbers(list_of_numbers)

    print("The Value at position 0 is: {:d}".format(value_at_position_0))


# before running the program, r
# eplace position 1 with the value 12
# and replace position 2 with the value 2.
def setup_list_correctly(list_of_numbers):
    list_of_numbers[1] = 12
    list_of_numbers[2] = 2


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
