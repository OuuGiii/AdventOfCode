import os
from helper.file_helper import read_helper
from helper.list_helper import list_helper

dirname = os.path.dirname(__file__)
FILE_NAME = os.path.join(dirname, 'data.txt')

CENTER_OF_MASS = "COM"
YOU = "YOU"
SANTA = "SAN"


def main():
    lists_of_strings = read_helper.read_file_by_row_and_split_by_character_and_return_lists_of_strings(
        FILE_NAME, ")")

    dictionary_of_children = create_dictionary_of_children(lists_of_strings)
    closest_parent_to_you_and_santa = find_closest_parent_to_you_and_santa(
        dictionary_of_children)
    orbits_between_you_and_santa = calculate_orbits_between_you_and_santa(
        closest_parent_to_you_and_santa, dictionary_of_children)

    print("\nThe total amount of orbits between you and santa is: {}".format(
        orbits_between_you_and_santa))


def create_dictionary_of_children(lists_of_strings):
    dictionary_of_children = {}

    for a_list in lists_of_strings:
        parent = a_list[0]
        child = a_list[1].strip()

        dictionary_of_children[child] = parent

    return dictionary_of_children


def find_closest_parent_to_you_and_santa(dictionary_of_children):
    dictionary_of_your_parents = find_parents_for_child(
        YOU, dictionary_of_children, {})
    dictionary_of_santas_parents = find_parents_for_child(
        SANTA, dictionary_of_children, {})

    for parent in dictionary_of_your_parents:
        if parent in dictionary_of_santas_parents:
            print("The closest parent between you and santa is: {:s}".format(
                parent))
            return parent


def find_parents_for_child(child, dictionary_of_children,
                           dictionary_of_parents):
    parent = dictionary_of_children[child]
    dictionary_of_parents[parent] = 0

    if dictionary_of_children[child] == CENTER_OF_MASS:
        return dictionary_of_parents

    child = parent

    return find_parents_for_child(child, dictionary_of_children,
                                  dictionary_of_parents)


def calculate_orbits_between_you_and_santa(closest_parent_to_you_and_santa,
                                           dictionary_of_children):
    total_orbits = 0
    orbits = 0

    orbits_from_you_to_parent = calculate_orbits_from_child_to_parent(
        YOU, closest_parent_to_you_and_santa, dictionary_of_children, orbits)
    print("Orbits from YOU to closest parent: {:d}".format(
        orbits_from_you_to_parent))

    orbits_from_santa_to_parent = calculate_orbits_from_child_to_parent(
        SANTA, closest_parent_to_you_and_santa, dictionary_of_children, orbits)
    print("Orbits from SAN to closest parent: {:d}".format(
        orbits_from_santa_to_parent))

    total_orbits = orbits_from_you_to_parent + orbits_from_santa_to_parent

    return total_orbits


def calculate_orbits_from_child_to_parent(child, parent,
                                          dictionary_of_children, orbits):
    if dictionary_of_children[child] == parent:
        return orbits
    else:
        orbits += 1
        child = dictionary_of_children[child]
        return calculate_orbits_from_child_to_parent(child, parent,
                                                     dictionary_of_children,
                                                     orbits)


main()
