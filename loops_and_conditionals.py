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

number = 5
isEven = "Yes" if number % 2 == 0 else "No"


def perform_math_operation():
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))
    operation = input("Enter operation (+, -, *, /): ")
    if operation == "+":
        result = number1 + number2
    elif operation == "-":
        result = number1 - number2
    elif operation == "*":
        result = number1 * number2
    elif operation == "/":
        result = number1 / number2
    else:
        result = "Invalid operation"
    print("Result:", result)


perform_math_operation()

i = 45
if i % 2:
    print("Odd number")
else:
    print("Even number")

for ch in "Hello World":
    print(ch)

for word in "Hello World".split():
    print(word)

for item in (3, 8, 9):
    print(item)


def print_squares_up_to(value):
    val = 1
    while val * val < value:
        print(val * val, end=" ")
        val += 1
    print()


print_squares_up_to(100)


def print_cubes_while_positive():
    number = int(input("Enter a number: "))

    while number >= 0:
        print(f"Cube is {number ** 3}")
        number = int(input("Enter a number: "))


print_cubes_while_positive()
