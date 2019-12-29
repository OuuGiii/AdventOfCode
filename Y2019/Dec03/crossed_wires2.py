import os
from collections import defaultdict
from helper.file_helper import read_helper
from helper.list_helper import list_helper

dirname = os.path.dirname(__file__)
FILE_NAME = os.path.join(dirname, 'data.txt')


class DIRECTIONS():
    UP = "U"
    RIGHT = "R"
    DOWN = "D"
    LEFT = "L"


def main():
    lists_of_strings = read_helper.read_file_by_row_and_split_by_character_and_return_lists_of_strings(
        FILE_NAME, ",")
    wires_coordinates = draw_wires(lists_of_strings)
    #print(wires_coordinates)

    cross_points = get_cross_points(wires_coordinates)
    #print(cross_points)

    steps_to_cross_points = get_steps_to_cross_points(lists_of_strings,
                                                      cross_points)

    min_steps_to_intersection = calculate_min_steps(steps_to_cross_points)

    print("The minimum amount of steps to get to an intersection is: {:d}".
          format(min_steps_to_intersection))


def draw_wires(lists_of_strings):
    wires_coordinates = []

    for list_of_characters in lists_of_strings:
        wire_coordinates = defaultdict(list)
        x = 0
        y = 0
        for character in list_of_characters:
            direction = character[0]
            magnitude = int(character[1:])

            if direction == DIRECTIONS.UP:
                for i in range(0, magnitude):
                    y += 1
                    wire_coordinates[x].append(y)
            elif direction == DIRECTIONS.RIGHT:
                for i in range(0, magnitude):
                    x += 1
                    wire_coordinates[x].append(y)
            elif direction == DIRECTIONS.DOWN:
                for i in range(0, magnitude):
                    y -= 1
                    wire_coordinates[x].append(y)
            elif direction == DIRECTIONS.LEFT:
                for i in range(0, magnitude):
                    x -= 1
                    wire_coordinates[x].append(y)

        wires_coordinates.append(wire_coordinates)

    return wires_coordinates


def get_cross_points(wires_coordinates):
    cross_points = defaultdict(list)

    for i in range(0, len(wires_coordinates) - 1):
        wire1_coordinates = wires_coordinates[i]
        for j in range(i + 1, len(wires_coordinates)):
            wire2_coordinates = wires_coordinates[j]

            for x1, y1_list in wire1_coordinates.items():
                if x1 in wire2_coordinates:
                    for y1 in y1_list:
                        if y1 in wire2_coordinates[x1]:
                            cross_points[x1].append(y1)

    return cross_points


def get_steps_to_cross_points(lists_of_strings, cross_points):
    steps_to_cross_points = {}

    for x, y_list in cross_points.items():
        for y in y_list:
            steps_to_cross_points[x] = defaultdict(list)
            steps_to_cross_points[x][y].append(0)

    for list_of_characters in lists_of_strings:
        x = 0
        y = 0
        steps = 0
        for character in list_of_characters:
            direction = character[0]
            magnitude = int(character[1:])

            if direction == DIRECTIONS.UP:
                for i in range(0, magnitude):
                    y += 1
                    steps += 1
                    if (is_coordinates_on_cross_point(x, y, cross_points)):
                        steps_to_cross_points[x][y].append(steps)

            elif direction == DIRECTIONS.RIGHT:
                for i in range(0, magnitude):
                    x += 1
                    steps += 1
                    if (is_coordinates_on_cross_point(x, y, cross_points)):
                        steps_to_cross_points[x][y].append(steps)

            elif direction == DIRECTIONS.DOWN:
                for i in range(0, magnitude):
                    y -= 1
                    steps += 1
                    if (is_coordinates_on_cross_point(x, y, cross_points)):
                        steps_to_cross_points[x][y].append(steps)

            elif direction == DIRECTIONS.LEFT:
                for i in range(0, magnitude):
                    x -= 1
                    steps += 1
                    if (is_coordinates_on_cross_point(x, y, cross_points)):
                        steps_to_cross_points[x][y].append(steps)

    return steps_to_cross_points


def calculate_min_steps(steps_to_cross_points):
    min_steps = None

    for x, y_dict in steps_to_cross_points.items():
        for y, steps_list in y_dict.items():
            steps_to_xy = list_helper.get_sum_of_list(steps_list)

            if not min_steps:
                min_steps = steps_to_xy
            elif steps_to_xy < min_steps:
                min_steps = steps_to_xy

    return min_steps


def is_coordinates_on_cross_point(x, y, cross_points):
    if x in cross_points:
        if y in cross_points[x]:
            return True

    return False


main()
