# Can't overload methods
# def print_table():
#     print_table(5)


def print_table(table=5, start=1, end=10):
    for i in range(start, end + 1):
        print(f'{table} * {i} = {table * i}')


print_table()
print_table(6)
print_table(7, 31, 40)
