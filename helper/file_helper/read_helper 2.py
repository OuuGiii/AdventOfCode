def read_file_by_row_and_return_list_of_numbers(file_name):
    list_of_numbers = []
    with open(file_name, "r") as file:
        for line in file:
            number = int(line)
            list_of_numbers.append(number)

    return list_of_numbers


def read_file_by_row_and_return_list_of_strings(file_name):
    list_of_strings = []
    with open(file_name, "r") as file:
        for line in file:
            a_string = line
            list_of_strings.append(a_string)

    return list_of_strings


def read_file_and_split_by_character_and_return_list_of_numbers(
    file_name, character):
    list_of_numbers = []
    with open(file_name, "r") as file:
        for line in file:
            numbers = line.split(character)
            for number in numbers:
                list_of_numbers.append(int(number))

    return list_of_numbers


def read_file_by_row_and_split_by_character_and_return_lists_of_numbers(
    file_name, character):
    lists_of_numbers = []
    with open(file_name, "r") as file:
        for line in file:
            newList = [].copy()
            numbers = line.split(character)
            for number in numbers:
                newList.append(int(number))
            lists_of_numbers.append(newList)

    return lists_of_numbers


def read_file_by_row_and_split_by_character_and_return_lists_of_strings(
    file_name, character):
    lists_of_strings = []
    with open(file_name, "r") as file:
        for line in file:
            newList = [].copy()
            strings = line.split(character)
            for a_string in strings:
                newList.append(a_string)
            lists_of_strings.append(newList)

    return lists_of_strings


def read_file_of_numbersequance_and_return_list_of_numbers(file_name):
    list_of_numbers = []
    with open(file_name, "r") as file:
        for line in file:
            for character in line:
                number = int(character)
                list_of_numbers.append(number)

    return list_of_numbers