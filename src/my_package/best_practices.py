import random


def calculate(x, y, z):
    if x > 100:
        x = x * 2
    else:
        x = x + 10
    y = y**2
    z = z / 3
    result = x + y + z
    return result


def process_data(data):
    processed = []
    for item in data:
        if item > 0:
            for i in range(5):
                item = item + i
            processed.append(item)
    return processed


class MyClass:
    def __init__(self):
        self.a = 1
        self.b = 2

    def do_something(self):
        return self.a + self.b
