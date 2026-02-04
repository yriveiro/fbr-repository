def inefficient_string_concatenation(n):
    # Performance issue: using + for string concatenation in a loop
    result = ""
    for i in range(n):
        result += str(i)
    return result


def slow_list_operation(data):
    # Performance issue: multiple loops over the same data
    squares = []
    for item in data:
        squares.append(item**2)
    # Then filter
    filtered = []
    for square in squares:
        if square % 2 == 0:
            filtered.append(square)
    return filtered


def memory_leak_simulation():
    # Performance issue: accumulating large lists without cleanup
    big_list = []
    for i in range(10000):
        big_list.append([j for j in range(1000)])
    return big_list
