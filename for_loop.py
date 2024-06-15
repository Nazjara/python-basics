def print_squares_of_number_up_to(number):
    for i in range(1, number + 1):
        print(i * i)
    print()


def print_squares_of_even_number_up_to(number):
    for i in range(2, number * 2 + 1, 2):
        print(i * i)
    print()


def print_numbers_in_reverse(number):
    for i in range(number, 0, -1):
        print(i)
    print()


print_squares_of_number_up_to(10)
print_squares_of_even_number_up_to(10)
print_numbers_in_reverse(10)
