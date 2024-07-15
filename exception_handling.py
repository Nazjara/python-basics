# print(1/0)  # ZeroDivisionError: division by zero
# print(2 + '2')  # TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print(value)  # NameError: name 'value' is not defined
# values = [1, 2, 3]
# print(values.non_existing())  # AttributeError: 'list' object has no attribute 'non_existing'

try:
    i = 0
    print(10 / i)
except ZeroDivisionError as e:
    print(e)
except (TypeError, ValueError):
    print('Unsupported operand types')
except NameError:
    print('Variable is not defined')
except AttributeError:
    print('Object has no attribute')
else:  # this is executed when the exception is not thrown
    print(i)
finally:
    print('Closing loop')


class Amount:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def add(self, amount):
        if self.currency == amount.currency:
            self.amount += amount.amount
        else:
            raise CurrenciesDoNotMatchException(f'{self.currency} does not match {amount.currency}')


class CurrenciesDoNotMatchException(Exception):
    def __init__(self, message):
        super().__init__(message)


amount1 = Amount('EUR', 10)
amount2 = Amount('USD', 20)
print(amount1.add(amount2))
