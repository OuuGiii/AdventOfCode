from helper.type_helper import type_helper


class OpCode:

    # opcode = [store_at_position, second_attribute, first_attribute, code]
    def __init__(self, number):
        self.store_at_position = None
        self.second_attribute = None
        self.first_attribute = None
        self.code = None

        list_of_digits = list(str(number))
        length_of_list = len(list_of_digits)

        if length_of_list == 1:
            self.store_at_position = 0
            self.second_attribute = 0
            self.first_attribute = 0
            self.code = int(list_of_digits[0])

        if length_of_list == 2:
            self.store_at_position = 0
            self.second_attribute = 0
            self.first_attribute = 0
            self.code = int(str(list_of_digits[0]) + str(list_of_digits[1]))

        if length_of_list == 3:
            self.store_at_position = 0
            self.second_attribute = 0
            self.first_attribute = int(list_of_digits[0])
            self.code = int(str(list_of_digits[1]) + str(list_of_digits[2]))

        if length_of_list == 4:
            self.store_at_position = 0
            self.second_attribute = int(list_of_digits[0])
            self.first_attribute = int(list_of_digits[1])
            self.code = int(str(list_of_digits[2]) + str(list_of_digits[3]))

        opcode = [
            self.store_at_position, self.second_attribute,
            self.first_attribute, self.code
        ]
        # print("opcode: {}".format(opcode))

    # Opcode 1 adds together numbers read from two positions
    # and stores the result in a third position.
    # The three integers immediately after the opcode tell you these three positions -
    # the first two indicate the positions from which you should read the input values,
    # and the third indicates the position at which the output should be stored.
    def run_opcode1(self, i, list_of_numbers):
        position_of_number1 = list_of_numbers[i + 1]
        position_of_number2 = list_of_numbers[i + 2]
        store_position = list_of_numbers[i + 3]

        number1 = None
        number2 = None

        if self.first_attribute == _MODES.POSITION_MODE:
            number1 = list_of_numbers[position_of_number1]

        elif self.first_attribute == _MODES.IMMEDIATE_MODE:
            number1 = position_of_number1

        if self.second_attribute == _MODES.POSITION_MODE:
            number2 = list_of_numbers[position_of_number2]

        elif self.second_attribute == _MODES.IMMEDIATE_MODE:
            number2 = position_of_number2

        list_of_numbers[store_position] = number1 + number2

    # Opcode 2 multiply together numbers read from two positions
    # and stores the result in a third position.
    # The three integers immediately after the opcode tell you these three positions -
    # the first two indicate the positions from which you should read the input values,
    # and the third indicates the position at which the output should be stored.
    def run_opcode2(self, i, list_of_numbers):
        position_of_number1 = list_of_numbers[i + 1]
        position_of_number2 = list_of_numbers[i + 2]
        store_position = list_of_numbers[i + 3]

        number1 = None
        number2 = None

        if self.first_attribute == _MODES.POSITION_MODE:
            number1 = list_of_numbers[position_of_number1]

        elif self.first_attribute == _MODES.IMMEDIATE_MODE:
            number1 = position_of_number1

        if self.second_attribute == _MODES.POSITION_MODE:
            number2 = list_of_numbers[position_of_number2]

        elif self.second_attribute == _MODES.IMMEDIATE_MODE:
            number2 = position_of_number2

        list_of_numbers[store_position] = number1 * number2

    # Opcode 3 takes a single integer as input
    # and saves it to the position given by its only parameter.
    # For example, the instruction 3,50 would take an input value
    # and store it at address 50.
    def run_opcode3(self, i, list_of_numbers):
        input_number = input("Opcode3 happend, insert a single number:\n")

        while len(input_number) != 1 or type_helper.is_int(
                input_number) == False:
            input_number = input(
                "The number can only be a singel digit, try again:\n")

        store_position = list_of_numbers[i + 1]

        list_of_numbers[store_position] = int(input_number)

    # Opcode 3 automatic, takes a single integer as parameter
    # and saves it to the position given by its second parameter.
    # For example, the instruction 3,50 would take an input value
    # and store it at address 50.
    def run_opcode3_automatic(self, number, i, list_of_numbers):
        store_position = list_of_numbers[i + 1]
        list_of_numbers[store_position] = number

    # Opcode 4 outputs the value of its only parameter.
    # For example, the instruction 4,50
    # would output the value at address 50.
    def run_opcode4(self, i, list_of_numbers):
        position_of_number_to_print = list_of_numbers[i + 1]
        number_to_print = list_of_numbers[position_of_number_to_print]
        print("opcode4 output: {}".format(number_to_print))
        return number_to_print

    # Opcode 5 is jump-if-true: if the first parameter is non-zero,
    # it sets the instruction pointer to the value from the second parameter.
    # Otherwise, it does nothing.
    def run_opcode5(self, i, list_of_numbers):
        position_of_number1 = list_of_numbers[i + 1]
        position_of_number2 = list_of_numbers[i + 2]

        number1 = None
        number2 = None

        if self.first_attribute == _MODES.POSITION_MODE:
            number1 = list_of_numbers[position_of_number1]

        elif self.first_attribute == _MODES.IMMEDIATE_MODE:
            number1 = position_of_number1

        if self.second_attribute == _MODES.POSITION_MODE:
            number2 = list_of_numbers[position_of_number2]

        elif self.second_attribute == _MODES.IMMEDIATE_MODE:
            number2 = position_of_number2

        if (number1 != 0):
            return number2

        else:
            return i + 3

    # Opcode 6 is jump-if-false: if the first parameter is zero,
    # it sets the instruction pointer to the value from the second parameter.
    # Otherwise, it does nothing.
    def run_opcode6(self, i, list_of_numbers):
        position_of_number1 = list_of_numbers[i + 1]
        position_of_number2 = list_of_numbers[i + 2]

        number1 = None
        number2 = None

        if self.first_attribute == _MODES.POSITION_MODE:
            number1 = list_of_numbers[position_of_number1]

        elif self.first_attribute == _MODES.IMMEDIATE_MODE:
            number1 = position_of_number1

        if self.second_attribute == _MODES.POSITION_MODE:
            number2 = list_of_numbers[position_of_number2]

        elif self.second_attribute == _MODES.IMMEDIATE_MODE:
            number2 = position_of_number2

        if (number1 == 0):
            return number2

        else:
            return i + 3

    # Opcode 7 is less than: if the first parameter is less than the second parameter,
    # it stores 1 in the position given by the third parameter.
    # Otherwise, it stores 0.
    def run_opcode7(self, i, list_of_numbers):
        position_of_number1 = list_of_numbers[i + 1]
        position_of_number2 = list_of_numbers[i + 2]
        store_position = list_of_numbers[i + 3]

        number1 = None
        number2 = None

        if self.first_attribute == _MODES.POSITION_MODE:
            number1 = list_of_numbers[position_of_number1]

        elif self.first_attribute == _MODES.IMMEDIATE_MODE:
            number1 = position_of_number1

        if self.second_attribute == _MODES.POSITION_MODE:
            number2 = list_of_numbers[position_of_number2]

        elif self.second_attribute == _MODES.IMMEDIATE_MODE:
            number2 = position_of_number2

        list_of_numbers[store_position] = number1 * number2

        if (number1 < number2):
            list_of_numbers[store_position] = 1
        else:
            list_of_numbers[store_position] = 0

    # Opcode 8 is equals: if the first parameter is equal to the second parameter,
    # it stores 1 in the position given by the third parameter.
    # Otherwise, it stores 0.
    def run_opcode8(self, i, list_of_numbers):
        position_of_number1 = list_of_numbers[i + 1]
        position_of_number2 = list_of_numbers[i + 2]
        store_position = list_of_numbers[i + 3]

        number1 = None
        number2 = None

        if self.first_attribute == _MODES.POSITION_MODE:
            number1 = list_of_numbers[position_of_number1]

        elif self.first_attribute == _MODES.IMMEDIATE_MODE:
            number1 = position_of_number1

        if self.second_attribute == _MODES.POSITION_MODE:
            number2 = list_of_numbers[position_of_number2]

        elif self.second_attribute == _MODES.IMMEDIATE_MODE:
            number2 = position_of_number2

        list_of_numbers[store_position] = number1 * number2

        if (number1 == number2):
            list_of_numbers[store_position] = 1
        else:
            list_of_numbers[store_position] = 0


class CODES:
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    END = 99


class _MODES:
    POSITION_MODE = 0
    IMMEDIATE_MODE = 1