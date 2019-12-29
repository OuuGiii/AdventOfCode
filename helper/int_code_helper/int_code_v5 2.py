from helper.int_code_helper.op_code_v5 import OpCode, CODES


class IntCode:
    list_of_numbers = None
    last_output = None

    def __init__(self, list_of_numbers, first_input, second_input):
        i = 0
        first_input_used = False
        while i < len(list_of_numbers) - 1:
            opcode = OpCode(list_of_numbers[i])

            if opcode.code == CODES.ONE:
                opcode.run_opcode1(i, list_of_numbers)
                i += 4

            elif opcode.code == CODES.TWO:
                opcode.run_opcode2(i, list_of_numbers)
                i += 4

            elif opcode.code == CODES.THREE:
                # print(first_input_used)
                if first_input_used == False:
                    opcode.run_opcode3_automatic(first_input, i,
                                                 list_of_numbers)
                    # print("First input: {}".format(first_input))
                    first_input_used = True
                else:
                    opcode.run_opcode3_automatic(second_input, i,
                                                 list_of_numbers)
                    # print("Second input: {}".format(second_input))
                i += 2

            elif opcode.code == CODES.FOUR:
                output = opcode.run_opcode4(i, list_of_numbers)
                self.last_output = output
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

        self.list_of_numbers = list_of_numbers