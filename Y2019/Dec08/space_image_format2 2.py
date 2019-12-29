import os
from helper.file_helper import read_helper
from helper.list_helper import list_helper

from helper.int_code_helper.int_code_v6 import IntCode

dirname = os.path.dirname(__file__)
FILE_NAME = os.path.join(dirname, 'data.txt')

IMAGE_WIDTH = 25
IMAGE_HEIGHT = 6
BLACK = 0
WHITE = 1
TRANSPARENT = 2


def main():
    list_of_numbers = read_helper.read_file_of_numbersequance_and_return_list_of_numbers(
        FILE_NAME)

    layers = encrypt_space_image(list_of_numbers)

    layers_putted_together = put_layers_together(layers)

    space_image = get_space_image(layers_putted_together)

    print("The space imaged recieved from the elves is: \n{}".format(
        space_image))


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


def get_layer_name(layer_number):
    return "Layer" + str(layer_number)


def put_layers_together(layers):
    layers_putted_together = None
    # print(layers)

    for layer_name, layer_content in layers.items():
        if not layers_putted_together:
            layers_putted_together = layer_content.copy()
            print("{}: {}".format(layer_name, layer_content))
            print("\n")
            print("layers_putted_together: {}".format(layers_putted_together))
        for row in range(0, IMAGE_HEIGHT):
            for i in range(0, IMAGE_WIDTH):
                # print(layers_putted_together)
                # print("Row: " + str(row) + ", i: " + str(i))
                if layers_putted_together[row][i] == 2:
                    layers_putted_together[row][i] = layer_content[row][i]

    return layers_putted_together


def get_space_image(layers_putted_together):
    space_image = ""

    for row in layers_putted_together:
        for digit in row:
            space_image += str(digit)

        space_image += "\n"

    return space_image


main()
