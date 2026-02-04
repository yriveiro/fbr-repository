import random


def calculate(x, y, z):  # Poor naming: what does it calculate?
    # Long function with multiple responsibilities
    # No type hints
    # Magic numbers
    if x > 100:
        x = x * 2
    else:
        x = x + 10
    y = y**2
    z = z / 3
    result = x + y + z
    return result


def process_data(data):  # Vague name
    # No documentation
    # Nested loops without clarity
    processed = []
    for item in data:
        if item > 0:
            for i in range(5):  # Magic number
                item = item + i
            processed.append(item)
    return processed


class MyClass:  # Poor class naming
    def __init__(self):
        self.a = 1  # Poor attribute naming
        self.b = 2

    def do_something(self):  # Vague method name
        return self.a + self.b
