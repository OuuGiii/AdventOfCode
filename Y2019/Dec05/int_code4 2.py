import os
from helper.file_helper import read_helper
from helper.list_helper import list_helper
from Y2019.Dec05.OpCode_4 import OpCode, CODES

dirname = os.path.dirname(__file__)
FILE_NAME = os.path.join(dirname, 'data.txt')


def main():
    list_of_numbers = read_helper.read_file_and_split_by_character_and_return_list_of_numbers(
        FILE_NAME, ",")

    last_output = run_int_code_for_list_of_numbers(list_of_numbers)

    print("\nThe last ouput is: {}".format(last_output))


def setup_list(list_of_numbers, int1, int2):
    list_of_numbers[1] = int1
    list_of_numbers[2] = int2


def run_int_code_for_list_of_numbers(list_of_numbers):
    last_output = None

    i = 0
    while i < len(list_of_numbers) - 1:
        opcode = OpCode(list_of_numbers[i])

        if opcode.code == CODES.ONE:
            opcode.run_opcode1(i, list_of_numbers)
            i += 4

        elif opcode.code == CODES.TWO:
            opcode.run_opcode2(i, list_of_numbers)
            i += 4

        elif opcode.code == CODES.THREE:
            opcode.run_opcode3(i, list_of_numbers)
            i += 2

        elif opcode.code == CODES.FOUR:
            last_output = opcode.run_opcode4(i, list_of_numbers)
            i += 2

        elif opcode.code == CODES.FIVE:
            i = opcode.run_opcode5(i, list_of_numbers)

        elif opcode.code == CODES.SIX:
            i = opcode.run_opcode6(i, list_of_numbers)

        elif opcode.code == CODES.SEVEN:
            opcode.run_opcode7(i, list_of_numbers)
            i += 4

        elif opcode.code == CODES.EIGHT:
            opcode.run_opcode8(i, list_of_numbers)
            i += 4

        elif opcode.code == CODES.END:
            break

        else:
            i += 1

    return last_output


main()
