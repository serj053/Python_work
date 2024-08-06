def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(17, 'не строка', False)
print_params(25)
print_params(54, 'string')
print_params(101, 'next string', True)
print_params(b=25)
print_params(c=[1,2,3])

values_list = [2, 'string', True]
values_dict = {'a': 1, 'b': 'string', 'c': True}
print_params(*values_list)
print_params(**values_dict)

values_list2 = ['string', False]
print_params(*values_list2, 42)