import random

print(random.random())  # 0.17554568388464964
print(random.randint(1, 10))  # 7 (inclusive)
print(random.randrange(1, 25, 3))  # 19
print(random.choice(['apple', 'banana', 'cherry']))  # banana
print(random.sample(['apple', 'banana', 'cherry'], 2))  # ['cherry', 'apple']
print(random.choice('abcdefg'))  # c
