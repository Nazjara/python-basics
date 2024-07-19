from collections import namedtuple

Person = namedtuple('Person', ['name', 'age', 'gender'])
person = Person('John', 25, 'Male')
print(person.name)  # John
