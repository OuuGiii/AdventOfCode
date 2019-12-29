import os
from helper.file_helper import read_helper
from helper.list_helper import list_helper

from helper.int_code_helper.int_code_v6 import IntCode

dirname = os.path.dirname(__file__)
FILE_NAME = os.path.join(dirname, 'data.txt')

IMAGE_WIDTH = 25
IMAGE_HEIGHT = 6


def main():
    list_of_numbers = read_helper.read_file_of_numbersequance_and_return_list_of_numbers(
        FILE_NAME)

    layers = encrypt_space_image(list_of_numbers)

    layer_with_min_zeros = find_layer_with_min_zeros(layers)
    print("\nThe layer with min zeros is: {:s}".format(layer_with_min_zeros))

    code_to_elves = get_code_from_layer(layers[layer_with_min_zeros])
    print("The code the elves wants is: {:d}".format(code_to_elves))


def encrypt_space_image(list_of_numbers):
    layers = {}

    width = 0
    height = 0
    layer_number = 1
    layer_name = "Layer"
    row = []
    layer = []

    for number in list_of_numbers:
        if (width == 25):
            height += 1
            width = 0

            layer.append(row.copy())
            row = []

        if (height == 6):
            height = 0

            layers[get_layer_name(layer_number)] = layer

            layer_number += 1
            layer = []

        row.append(number)
        width += 1

    return layers


def find_layer_with_min_zeros(layers):
    layer_with_min_zeros = None
    min_zeros = None

    for layer_name, layer_content in layers.items():
        amount_of_zeros = 0
        # print(layer_name)
        # print(
        #     "=======================================\n================================"
        # )
        for row in layer_content:
            for digit in row:
                if digit == 0:
                    amount_of_zeros += 1

        print("{} has this many zeros: {}".format(layer_name, amount_of_zeros))
        if not min_zeros or amount_of_zeros < min_zeros:
            min_zeros = amount_of_zeros
            layer_with_min_zeros = layer_name
            #print(min_zeros)

    return layer_with_min_zeros


def get_layer_name(layer_number):
    return "Layer" + str(layer_number)


def get_code_from_layer(layer):
    number_of_ones = 0
    number_of_twos = 0

    for row in layer:
        for digit in row:
            if digit == 1:
                number_of_ones += 1
            elif digit == 2:
                number_of_twos += 1

    print(number_of_ones)
    print(number_of_twos)

    return number_of_ones * number_of_twos


main()
