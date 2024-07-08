class Leisure:
    def enjoy(self):
        print("Leisure enjoy")


class Book:

    def __init__(self, name, number_of_copies=5):
        self.name = name
        self.number_of_copies = number_of_copies

    def increase_number_of_copies(self, how_much):
        self.number_of_copies += how_much

    def decrease_number_of_copies(self, how_much):
        self.number_of_copies -= how_much

    def __repr__(self):
        return repr((self.name, self.number_of_copies))


class Romance(Book, Leisure):

    def __init__(self, is_contemporary, is_comedy, name, number_of_copies):
        super().__init__(name, number_of_copies)
        self.is_contemporary = is_contemporary
        self.is_comedy = is_comedy

    def __repr__(self):
        return repr((super().__repr__(), self.is_contemporary, self.is_comedy))


if __name__ == "__main__":
    book1 = Book('Some book 1', 10)
    book1.increase_number_of_copies(3)

    book2 = Book('Some book 2')
    book2.decrease_number_of_copies(3)

    book3 = Romance(is_contemporary=False, is_comedy=True, name='Romance book', number_of_copies=3)
    book3.increase_number_of_copies(5)

    print(book1)  # ('Some book 1', 13)
    print(book2)  # ('Some book 2', 2)
    print(book3)  # ("('Romance book', 8)", False, True)

# Abstract class
from abc import ABC, abstractmethod


class AbstractClass(ABC):
    def basic_method(self):
        print('Basic method')
        self.abstract_method1()
        self.abstract_method2()

    @abstractmethod
    def abstract_method1(self):
        pass

    @abstractmethod
    def abstract_method2(self):
        pass


class ImplementationClass(AbstractClass):

    value = 0  # static variable

    @staticmethod
    def static_method():
        print("Static method")

    def abstract_method1(self):
        print("Abstract method 1 implementation")

    def abstract_method2(self):
        print('Abstract method 2 implementation')

