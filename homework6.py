my_dict = {"name":"Sergey", "age": 61, "email":"serj053@rambler.ru"}
print(my_dict)
print(my_dict['name'])
my_dict['city'] = "Barnaul"
print(my_dict)
my_dict.update({"job":"engineer", "salary": 100_000})
print(my_dict)
print(my_dict.pop("city"))
print(my_dict)
#############################################################
my_set = {3, 3, 3, "str", "name", (1, 2, 3), "str"}
print(my_set)
my_set.add('book')
print(my_set)
my_set.remove('name')
print(my_set)


