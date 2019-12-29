from helper.type_helper import type_helper
from helper.int_code_helper.version7.constants.codes import CODES
from helper.int_code_helper.version7.op_code import OpCode


class IntCode:
    def __init__(self, list_of_numbers):
        self.list_of_numbers = list_of_numbers
        self.last_output = None
        self.current_position = 0
        self.has_ended = False
        self.inputs = []

    def run_intCode(self, automatic=False):
        while self.current_position < len(self.list_of_numbers):
            opcode = OpCode(self.list_of_numbers[self.current_position])

            if opcode.code == CODES.ONE:
                opcode.run_opcode1(self.current_position, self.list_of_numbers)
                self.current_position += 4

            elif opcode.code == CODES.TWO:
                opcode.run_opcode2(self.current_position, self.list_of_numbers)
                self.current_position += 4

            elif opcode.code == CODES.THREE:
                if automatic:
                    if not self.inputs:
                        print("No input, current position is {}".format(
                            self.current_position))
                        print(self.inputs)
                        return

                    else:
                        input_to_use = self.inputs[0]
                        self.inputs = self.inputs[1:]
                        opcode.run_opcode3_automatic(input_to_use,
                                                     self.current_position,
                                                     self.list_of_numbers)
                        if input_to_use == 3027478:
                            print("Current pos: {}".format(
                                self.current_position))
                            print(self.list_of_numbers[429:])
                        self.current_position += 2

                else:
                    opcode.run_opcode3(self.current_position,
                                       self.list_of_numbers)

            elif opcode.code == CODES.FOUR:
                output = opcode.run_opcode4(self.current_position,
                                            self.list_of_numbers)
                self.last_output = output
                self.current_position += 2

            elif opcode.code == CODES.FIVE:
                self.current_position = opcode.run_opcode5(
                    self.current_position, self.list_of_numbers)

            elif opcode.code == CODES.SIX:
                self.current_position = opcode.run_opcode6(
                    self.current_position, self.list_of_numbers)

            elif opcode.code == CODES.SEVEN:
                opcode.run_opcode7(self.current_position, self.list_of_numbers)
                self.current_position += 4

            elif opcode.code == CODES.EIGHT:
                opcode.run_opcode8(self.current_position, self.list_of_numbers)
                self.current_position += 4

            elif opcode.code == CODES.NINE:
                opcode.run_opcode9(self.current_position, self.list_of_numbers)
                self.current_position += 2

            elif opcode.code == CODES.END:
                self.has_ended = True
                self.current_position
                return

            else:
                self.current_position += 1