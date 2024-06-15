print(type(10))  # int
print(type(10.50))  # float
print(type(True))  # bool
print(type("Text"))  # str
print(type('Text'))  # str
print(type([1, 2]))  # list

# Dynamic typing (type is inferred from the value)
value = "Value"
print(type(value))  # str
print(len(value))  # 5
value = 1
print(type(value))  # int
# print(len(value))  # TypeError: object of type 'int' has no len()

# Type of numeric operation results
number1 = 10
number2 = 20
print(type(number2 / number1))  # float
print(type(number2 // number1))  # int

# Boolean values conversion
print(bool('True'))  # True
print(bool('False'))  # True
print(bool(''))  # False

# Integer values conversion
print(int('45'))  # 45
# print(int('45.56'))  # ValueError: invalid literal for int() with base 10: '45.56'
print(int('45abc', 15))  # 221802
