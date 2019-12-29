# Wanted to test that new lists are created and not using the same one
from collections import defaultdict
from enum import Enum


def new_list_test():
    lists = []

    for i in range(0, 5):
        a_list = []
        a_dict = defaultdict(list)
        for j in range(1, 6):
            a_list.append(i + j)
            a_dict[i].append(j)
        lists.append(a_list)
        lists.append(a_dict)
        for key, value in a_dict.items():
            print("key: {}, value: {}".format(key, value))

    print(lists)


def string_part_test():
    a_string = "U29"

    direction = a_string[0]
    magnitude = int(a_string[1:])

    print("direction: {:s}, magnitude: {:d}".format(direction, magnitude))


# DIDN'T WORK
def dict_test():
    STUFF = {a: "kakka", b: "shit", c: "rippe"}
    print(STUFF.a)


def enum_test():
    class STUFF():
        a = "kakka"
        b = "shit"
        c = "rippe"

    #STUFF2 = Enum(a="kakka", b="shit")

    print(STUFF.a)
    #print(STUFF2.a)


new_list_test()
string_part_test()
#dict_test()
enum_test()
