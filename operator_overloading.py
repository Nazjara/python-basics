from functools import total_ordering


@total_ordering
class Money:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __add__(self, other):
        return Money(self.currency, self.amount + other.amount)

    def __sub__(self, other):
        return Money(self.currency, self.amount - other.amount)

    def __mul__(self, other):
        return Money(self.currency, self.amount * other.amount)

    def __truediv__(self, other):
        return Money(self.currency, self.amount / other.amount)

    def __eq__(self, other):
        return (self.currency, self.amount) == (other.currency, other.amount)

    def __lt__(self, other):
        return self.amount < other.amount

    # def __ne__(self, other):
    #     return (self.currency, self.amount) != (other.currency, other.amount)

    # def __gt__(self, other):
    #     return self.amount > other.amount

    # def __le__(self, other):
    #     return self.amount <= other.amount

    # def __ge__(self, other):
    #     return self.amount >= other.amount

    def __repr__(self):
        return f'Money({self.currency}, {self.amount})'


amount1 = Money('USD', 100)
amount2 = Money('USD', 200)
print(amount1 + amount2)  # Money(USD, 300)
print(amount2 - amount1)  # Money(USD, 100)
print(amount1 * amount2)  # Money(USD, 20000)
print(amount2 / amount1)  # Money(USD, 2.0)
print(amount1 == amount2)  # False
print(amount1 < amount2)  # True
print(amount2 <= amount1)  # False
