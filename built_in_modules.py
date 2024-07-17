import math
from math import sqrt
from decimal import Decimal
import statistics
from collections import deque
import datetime

print(math.factorial(5))  # 120
print(sqrt(5))  # 2.23606797749979
print(math.pi)  # 3.141592653589793
print(math.e)  # 2.718281828459045

print(Decimal('4.5') - Decimal('3.2'))  # 1.3

marks = [1, 6, 9, 23, 2]

print(statistics.median(marks))  # 6
print(statistics.mean(marks))  # 8.2
print(statistics.variance(marks))  # 78.7

queue = deque(marks)
print(queue)  # deque([1, 6, 9, 23, 2])
print(queue.pop())  # 2
print(queue)  # deque([1, 6, 9, 23])
queue.append(99)
print(queue)  # deque([1, 6, 9, 23, 99])
print(queue.popleft())  # 1
print(queue)  # deque([6, 9, 23, 99])
queue.appendleft(128)
print(queue)  # deque([128, 6, 9, 23, 99])

print(datetime.datetime.now())  # 2024-07-17 23:16:46.841444
print(datetime.datetime.today().year)  # 2024
print(datetime.datetime.today().second)  # 12
print(datetime.datetime(2024, 7, 17))  # 2024-07-17 00:00:00
print(datetime.datetime(2024, 7, 17) + datetime.timedelta(days=10))  # 2024-07-27 00:00:00
