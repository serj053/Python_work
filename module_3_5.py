def get_multipliet_digit(namber):
    str_number = str(namber)
    if len(str_number) < 2:
        return int(str_number)
    first = int(str_number[0])
    return first * get_multipliet_digit(int(str_number[1:]))


print(get_multipliet_digit(40203))