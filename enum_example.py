from enum import Enum


class Currency(Enum):
    USD = 1
    EUR = 2
    UAH = 3


for currency in Currency:
    print(currency)  # Currency.USD, Currency.EUR, Currency.UAH

print(Currency(1).name)  # USD
print(Currency(1).value)  # 1
