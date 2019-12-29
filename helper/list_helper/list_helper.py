def get_sum_of_list(list_of_numbers):
    sum = 0
    for number in list_of_numbers:
        sum += number

    return sum


def print_how_many_times_items_repeats_in_list(a_list):
    for item1 in a_list:
        x = 0
        for item2 in a_list:
            if item1 == item2:
                x += 1
        print("{} appeared: {} times".format(item1, x))


def find_first_item_repeated_in_list(a_list):
    for item1 in a_list:
        x = 0
        for item2 in a_list:
            if item1 == item2:
                x += 1
        if x > 1:
            return item1


def find_min_value_in_list(list_of_numbers):
    min_value = None

    for value in list_of_numbers:
        if not min_value:
            min_value = value
        elif value < min_value:
            min_value = value

    return min_value


def find_max_value_in_list(list_of_numbers):
    max_value = None

    for value in list_of_numbers:
        if not max_value:
            max_value = value
        elif value > max_value:
            max_value = value

    return max_value


def find_closest_to_zero_value_in_list(list_of_numbers):
    closest_to_zero_value = None

    for value in list_of_numbers:
        if not closest_to_zero_value:
            closest_to_zero_value = abs(value)
        elif abs(value) < closest_to_zero_value:
            closest_to_zero_value = abs(value)

    return closest_to_zero_value


def reverse_list(a_list):
    reverse_list = []

    for i in range(len(a_list) - 1, -1, -1):
        reverse_list.append(a_list[i])

    return reverse_list


def how_many_times_does_item_occure_in_list(a_item, a_list):
    occurance = 0
    for element in a_list:
        if element == a_item:
            occurance += 1

    return occurance