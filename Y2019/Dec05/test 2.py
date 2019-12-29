def is_int(number):
    try:
        int(number)
        return True
    except ValueError:
        return False


input_number = input("input:")
print(is_int(input_number))