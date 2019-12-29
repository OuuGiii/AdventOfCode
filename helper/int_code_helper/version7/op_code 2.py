from helper.int_code_helper.version7.constants.modes import MODES


class OpCode:

    # opcode = [store_at_position, second_attribute, first_attribute, code]
    def __init__(self, number):
        self.store_at_position = None
        self.second_attribute = None
        self.first_attribute = None
        self.code = None
        self.relative_base = None

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

        number1 = self._get_number_from_mode(self.first_attribute,
                                             position_of_number1,
                                             list_of_numbers)
        number2 = self._get_number_from_mode(self.second_attribute,
                                             position_of_number2,
                                             list_of_numbers)

        self._store_in_list(list_of_numbers, store_position, number1 + number2)

    # Opcode 2 multiply together numbers read from two positions
    # and stores the result in a third position.
    # The three integers immediately after the opcode tell you these three positions -
    # the first two indicate the positions from which you should read the input values,
    # and the third indicates the position at which the output should be stored.
    def run_opcode2(self, i, list_of_numbers):
        position_of_number1 = list_of_numbers[i + 1]
        position_of_number2 = list_of_numbers[i + 2]
        store_position = list_of_numbers[i + 3]

        number1 = self._get_number_from_mode(self.first_attribute,
                                             position_of_number1,
                                             list_of_numbers)
        number2 = self._get_number_from_mode(self.second_attribute,
                                             position_of_number2,
                                             list_of_numbers)

        self._store_in_list(list_of_numbers, store_position, number1 * number2)

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

        self._store_in_list(list_of_numbers, store_position, int(input_number))

    # Opcode 3 automatic, takes a single integer as parameter
    # and saves it to the position given by its second parameter.
    # For example, the instruction 3,50 would take an input value
    # and store it at address 50.
    def run_opcode3_automatic(self, number, i, list_of_numbers):
        store_position = list_of_numbers[i + 1]
        self._store_in_list(list_of_numbers, store_position, number)

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

        number1 = self._get_number_from_mode(self.first_attribute,
                                             position_of_number1,
                                             list_of_numbers)
        number2 = self._get_number_from_mode(self.second_attribute,
                                             position_of_number2,
                                             list_of_numbers)

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

        number1 = self._get_number_from_mode(self.first_attribute,
                                             position_of_number1,
                                             list_of_numbers)
        number2 = self._get_number_from_mode(self.second_attribute,
                                             position_of_number2,
                                             list_of_numbers)

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

        number1 = self._get_number_from_mode(self.first_attribute,
                                             position_of_number1,
                                             list_of_numbers)
        number2 = self._get_number_from_mode(self.second_attribute,
                                             position_of_number2,
                                             list_of_numbers)

        self._store_in_list(list_of_numbers, store_position, number1 * number2)

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

        number1 = self._get_number_from_mode(self.first_attribute,
                                             position_of_number1,
                                             list_of_numbers)
        number2 = self._get_number_from_mode(self.second_attribute,
                                             position_of_number2,
                                             list_of_numbers)

        self._store_in_list(list_of_numbers, store_position, number1 * number2)

        if (number1 == number2):
            list_of_numbers[store_position] = 1
        else:
            list_of_numbers[store_position] = 0

    # Opcode 9 adjusts the relative base by the value of its only parameter.
    # The relative base increases (or decreases, if the value is negative)
    # by the value of the parameter.
    def run_opcode9(self, i, list_of_numbers):
        self.relative_base += self._get_number_from_list(
            list_of_numbers, i + 1)

    def _get_number_from_mode(self, mode, number, list_of_numbers):
        if mode == MODES.POSITION_MODE:
            number_to_return = list_of_numbers[number]

        elif mode == MODES.IMMEDIATE_MODE:
            number_to_return = number

        elif mode == MODES.RELATIVE_MODE:
            relative_position = self.relative_base + number
            number_to_return = list_of_numbers[relative_position]

        return number_to_return

    def _store_in_list(self, list_of_numbers, position, number):
        while True:
            try:
                list_of_numbers[position] = number
                break
            except IndexError as identifier:
                space_needed = position - (len(list_of_numbers) - 1)
                print("Adding {} zeros".format(space_needed))
                i = 0
                while i < space_needed:
                    list_of_numbers.append(0)
                    i += 1

    # Maybe just make list big in beginning, no need for checking this and the above one
    def _get_number_from_list(self, list_of_numbers, position):
        try:
            return list_of_numbers[position]
        except IndexError as identifier:
            return 0