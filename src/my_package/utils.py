def inefficient_string_concatenation(n):
    result = ""
    for i in range(n):
        result += str(i)
    return result


def slow_list_operation(data):
    squares = []
    for item in data:
        squares.append(item**2)
    filtered = []
    for square in squares:
        if square % 2 == 0:
            filtered.append(square)
    return filtered


def memory_leak_simulation():
    big_list = []
    for i in range(10000):
        big_list.append([j for j in range(1000)])
    return big_list
