import os
from helper.file_helper import read_helper
from helper.list_helper import list_helper

dirname = os.path.dirname(__file__)
FILE_NAME = os.path.join(dirname, 'data.txt')

CENTER_OF_MASS = "COM"


def main():
    lists_of_strings = read_helper.read_file_by_row_and_split_by_character_and_return_lists_of_strings(
        FILE_NAME, ")")

    dictionary_of_children = create_dictionary_of_children(lists_of_strings)
    dictionary_of_orbits_per_child = calculate_orbits_per_child(
        dictionary_of_children)
    total_orbits = count_total_orbits(dictionary_of_orbits_per_child)

    print("\nThe total amount of orbits are: {}".format(total_orbits))


def create_dictionary_of_children(lists_of_strings):
    dictionary_of_children = {}

    for a_list in lists_of_strings:
        parent = a_list[0]
        child = a_list[1].strip()

        dictionary_of_children[child] = parent

    return dictionary_of_children


def calculate_orbits_per_child(dictionary_of_children):
    dictionary_of_orbits_per_child = {}

    for child, parent in dictionary_of_children.items():
        orbits = 0
        orbits_around_child = count_orbit_for_child(child, parent,
                                                    dictionary_of_children,
                                                    orbits)

        dictionary_of_orbits_per_child[child] = orbits_around_child
        #print("{} : {}".format(child, parent))

    return dictionary_of_orbits_per_child


def count_orbit_for_child(child, parent, dictionary_of_children, orbits):
    orbits += 1

    if parent == CENTER_OF_MASS:
        return orbits
    child = parent
    parent = dictionary_of_children[parent]
    return count_orbit_for_child(child, parent, dictionary_of_children, orbits)


def count_total_orbits(dictionary_of_orbits_per_child):
    total_orbits = 0

    for child, orbits in dictionary_of_orbits_per_child.items():
        total_orbits += orbits
        #print("{} : {}".format(child, orbits))

    return total_orbits


main()
