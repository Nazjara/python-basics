class List:  # ordered, mutable collection of elements, []
    marks = [23, 56, 67]
    print(sum(marks))  # 146
    print(max(marks))  # 67
    print(min(marks))  # 23
    print(len(marks))  # 3
    marks.append(76)
    print(marks)  # [23, 56, 67, 76]
    marks.insert(2, 77)
    print(marks)  # [23, 56, 77, 67, 76]
    marks.remove(77)
    print(77 in marks)  # False
    print(marks.index(67))  # 2
    # print(marks.index(99))  # ValueError: 99 is not in list

    animals = ['Cat', 'Dog', 'Elephant']
    animals.append('Fish')
    print(animals)  # ['Cat', 'Dog', 'Elephant', 'Fish']
    animals.remove('Dog')
    print(animals)  # ['Cat', 'Elephant', 'Fish']
    print(animals[2])  # Fish
    # print(animals[4])  # IndexError: list index out of range
    del animals[2]
    print(animals)  # ['Cat', 'Elephant']
    animals.extend('Mouse')
    print(animals)  # ['Cat', 'Elephant', 'M', 'o', 'u', 's', 'e']
    animals.extend(['Bird', 'Horse'])
    print(animals)  # ['Cat', 'Elephant', 'M', 'o', 'u', 's', 'e', 'Bird', 'Horse']
    animals.append('Mouse')
    print(animals)  # ['Cat', 'Elephant', 'M', 'o', 'u', 's', 'e', 'Bird', 'Horse', 'Mouse']
    animals += ['Rabbit', 'Beaver']
    print(animals)  # ['Cat', 'Elephant', 'M', 'o', 'u', 's', 'e', 'Bird', 'Horse', 'Mouse', 'Rabbit', 'Beaver']
    animals.append(10)
    print(animals)  # ['Cat', 'Elephant', 'M', 'o', 'u', 's', 'e', 'Bird', 'Horse', 'Mouse', 'Rabbit', 'Beaver', 10]

    numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    print(numbers[2:6])  # ['three', 'four', 'five', 'six']
    print(numbers[:6])  # ['one', 'two', 'three', 'four', 'five', 'six']
    print(numbers[3:])  # ['four', 'five', 'six', 'seven', 'eight', 'nine']
    print(numbers[1:8:3])  # ['two', 'five', 'eight']
    print(numbers[::3])  # ['one', 'four', 'seven']
    print(numbers[::-1])  # ['nine', 'eight', 'seven', 'six', 'five', 'four', 'three', 'two', 'one']
    print(numbers[::-3])  # ['nine', 'six', 'three']
    del numbers[3:]
    print(numbers)  # ['one', 'two', 'three']
    numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    del numbers[5:7]
    print(numbers)  # ['one', 'two', 'three', 'four', 'five', 'eight', 'nine']
    numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    numbers[2:6] = [3, 4, 5, 6]
    print(numbers)  # ['one', 'two', 'three', 3, 4, 5, 6, 'eight', 'nine']

    numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    numbers.reverse()
    print(numbers)  # numbers.reverse()
    numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for number in reversed(numbers):
        print(number)  # nine, eight, seven, six, five, four, three, two, one
    numbers.sort(key=len)
    print(numbers)  # ['one', 'two', 'six', 'four', 'five', 'nine', 'three', 'seven', 'eight']
    numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for number in sorted(numbers, key=len, reverse=True):
        print(number)  # three, seven, eight, four, five, nine, one, two, six

    numbers = [1, 2, 3, 4]
    print(numbers.pop())  # 4
    print(numbers)  # [1, 2, 3]
    print(numbers.pop(0))  # 1
    print(numbers)  # [2, 3]

    class Country:
        def __init__(self, name, population, area):
            self.name = name
            self.population = population
            self.area = area

        def __repr__(self):
            return repr((self.name, self.population, self.area))

    countries = [Country('Ukraine', 38, 603),
                 Country('Spain', 48, 506),
                 Country('France', 68, 551)]

    print(countries)  # [('Ukraine', 38, 603), ('Spain', 48, 506), ('France', 68, 551)]
    countries.sort(key=lambda x: x.population, reverse=False)
    print(countries)  # [('Ukraine', 38, 603), ('Spain', 48, 506), ('France', 68, 551)]

    numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    numbers_length = [len(number) for number in numbers]
    print(numbers_length)  # [3, 3, 5, 4, 4, 3, 5, 5, 4]
    numbers_length_four = [number for number in numbers if len(number) == 4]  # list comprehension
    print(numbers_length_four)  # ['four', 'five', 'nine']


class Set:   # unordered, mutable collection of elements, {}
    numbers = [1, 2, 3, 2, 1]
    numbers_set = set(numbers)
    print(numbers_set)  # {1, 2, 3}
    numbers_set.add(2)
    print(numbers_set)  # {1, 2, 3}
    numbers_set.add(4)
    print(numbers_set)  # {1, 2, 3, 4}
    numbers_set.remove(4)
    print(numbers_set)  # {1, 2, 3}

    numbers_1_to_5_set = set(range(1, 6))
    print(numbers_1_to_5_set)  # {1, 2, 3, 4, 5}
    numbers_4_to_10_set = set(range(4, 11))
    print(numbers_4_to_10_set)  # {4, 5, 6, 7, 8, 9, 10}
    print(numbers_1_to_5_set | numbers_4_to_10_set)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    print(numbers_1_to_5_set & numbers_4_to_10_set)  # {4, 5}
    print(numbers_1_to_5_set - numbers_4_to_10_set)  # {1, 2, 3}
    squares_first_ten_numbers_set = {i * i for i in range(1, 11)}  # set comprehension
    print(squares_first_ten_numbers_set)  # {64, 1, 4, 36, 100, 9, 16, 49, 81, 25}


class Dictionary:    # ordered, mutable collection of key-value pairs, {}
    occurrences = dict(a=5, b=6, c=8)
    print(occurrences)  # {'a': 5, 'b': 6, 'c': 8}
    print(occurrences.keys())  # dict_keys(['a', 'b', 'c'])
    print(occurrences.values())  # dict_values([5, 6, 8])
    print(occurrences.items())  # dict_items([('a', 5), ('b', 6), ('c', 8)])
    print(occurrences.get('c'))  # 8
    print(occurrences.get('d', 'default'))  # default
    for (k, v) in occurrences.items():
        print(f'{k}: {v}')  # a: 5 b: 6 c: 8
    del occurrences['c']
    print(occurrences)  # {'a': 5, 'b': 6}
    squares_first_ten_numbers_dict = {i: i * i for i in range(1, 11)}  # dictionary comprehension
    print(squares_first_ten_numbers_dict)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}


class Tuple:   # ordered, immutable collection of elements, ()
    country = ('Ukraine', 38, 603)
    print(country)  # ('Ukraine', 38, 603)
    print(country[1])  # 38
    # country[1] = 'France'  # TypeError: 'tuple' object does not support item assignment
    name, population, area = country
    print(f'{name}, {population}, {area}')  # Ukraine, 38, 603

