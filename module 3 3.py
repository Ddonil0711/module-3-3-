def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


print_params(33, 22)
print_params(a=1, c=5,)
print_params(b=25)
print_params(c = [1,2,3])

values_list = [1, 'balls', True]
values_dict = {'a':3, 'b':False, 'c':'str'}


print_params(*values_list)
print_params(**values_dict)

value_list2 = [1, True]
print_params(*value_list2, 42)