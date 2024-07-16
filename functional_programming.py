from functools import reduce


def multiply_by_2(data):
    return data * 2


def do_and_print(func, data):
    print(func(data))


do_and_print(multiply_by_2, 10)  # 20

function_reference = multiply_by_2
print(function_reference(10))  # 20

do_and_print(lambda data: data * data, 10)  # 100
do_and_print(lambda data: len(data), 'Test')  # 4

numbers = [1, 2, 3, 4, 5]
words = ['Apple', 'Ant', 'Bat']

filtered_list = list(filter(lambda x: x % 2 == 0, numbers))
print(filtered_list)  # [2, 4]
filtered_list = list(filter(lambda x: x.endswith('at'), words))
print(filtered_list)  # ['Bat']

mapped_list = list(map(lambda x: x.upper(), words))
print(mapped_list)  # ['APPLE', 'ANT', 'BAT']
mapped_list = list(map(lambda x: len(x), words))
print(mapped_list)  # [5, 3, 3]

print(reduce(lambda x, y: x + y, numbers))  # 15
print(reduce(lambda x, y: max(x, y), numbers))  # 5
print(reduce(lambda x, y: x if len(x) > len(y) else y, words))  # Apple

numbers = [3, 7, 8, 15, 24, 35, 46]

processed_list = reduce(lambda x, y: x + y,
                        map(lambda x: x * x,
                            filter(lambda x: x % 2 == 0, numbers)))

print(processed_list)  # 2756

months = [('January', 31), ('February', 28), ('March', 31)]

processed_list = reduce(lambda x, y: x + y, map(lambda x: x[1], months))
print(processed_list)  # 90
