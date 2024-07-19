class Book:
    def __init__(self, name, copies):
        self.name = name
        self._copies = copies

    @property
    def copies(self):
        print('Getter called')
        return self._copies

    @copies.setter
    def copies(self, value):
        print('Setter called')
        self._copies = value


microservices = Book('Microservices', 3)
print(microservices.copies)  # 3

microservices.copies = 10
print(microservices.copies)  # 10
