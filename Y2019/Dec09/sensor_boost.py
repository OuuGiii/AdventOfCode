import os
from helper.file_helper import read_helper
from helper.list_helper import list_helper

from helper.int_code_helper.version7.int_code import IntCode

dirname = os.path.dirname(__file__)
FILE_NAME = os.path.join(dirname, 'data.txt')


def main():
    list_of_numbers = read_helper.read_file_and_split_by_character_and_return_list_of_numbers(
        FILE_NAME, ",")

    boost = IntCode(list_of_numbers)

    boost.run_intCode()

    boost_key_code = boost.last_output

    print("\nThe BOOST key code is: {:d}".format(boost_key_code))


main()
