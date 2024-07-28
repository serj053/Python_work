print("Введите три числа:")
first   = input()
second = input()
third = input()
print(f"Вы ввели:  {first}, {second}, {third}")
if first == second and first == third and second == third:
    print(3)
elif first == second:
    print(2)
elif  first == third:
    print(2)
elif  second == third:
    print(2)
else:
    print(0)

