my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
while True:
    if my_list[i] >= 0:  # если считать 0 положительным числом.
        print(my_list[i])
        i = i + 1
        continue
    else:
        break

# elif my_list[i] < 0 or my_list[i] == len(my_list): - избыточный код
