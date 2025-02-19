def generate_diamond_loops(row_count):
    """
    Uses loops to generate a diamond pattern.
    :param row_count:   nth row midpoint
    """
    top_max = row_count * 2 - 1
    midpoint = top_max // 2 + 1

    for i in range(1, row_count + 1):
        ast = ''
        spaces = ''

        for _ in range(i * 2 - 1):
            ast += '*'
        for _ in range(midpoint - (i * 2 // 2)):
            spaces += ' '
        print(spaces + ast)

    for i in range(row_count - 1, 0, -1):
        ast = ''
        spaces = ''

        for _ in range(i * 2 - 1):
            ast += '*'
        for _ in range(midpoint - (i * 2 // 2)):
            spaces += ' '
        print(spaces + ast)


def generate_diamond_strings(row_count):
    """
    Uses string multiplication to generate a diamond pattern.
    :param row_count:   nth row midpoint
    """
    top_max = row_count * 2 - 1
    midpoint = top_max // 2 + 1

    for i in range(1, row_count + 1):
        ast = '*' * (i * 2 - 1)
        spaces = ' ' * (midpoint - (i * 2 // 2))
        print(spaces + ast)

    for i in range(row_count - 1, 0, -1):
        ast = '*' * (i * 2 - 1)
        spaces = ' ' * (midpoint - (i * 2 // 2))
        print(spaces + ast)


def generate_diamond_arithmetic(row_count):
    """
    Uses the arithmetic sequence formula: `n(x - 1) + a_1`
    to generate a diamond pattern.
    :param row_count:   nth row midpoint
    """
    # top_max = row_count * 2 - 1
    # midpoint = top_max // 2 + 1

    for i in range(1, row_count + 1):
        ast = '*' * (2 * (i - 1) + 1)
        spaces = ' ' * (-1 * (i - 1) + row_count - 1)
        print(spaces + ast)

    for i in range(row_count - 1, 0, -1):
        ast = '*' * (2 * (i - 1) + 1)
        spaces = ' ' * (-1 * (i - 1) + row_count - 1)
        print(spaces + ast)


# Generate diamond patterns
generate_diamond_loops(4)
print('------------------------------------')
generate_diamond_strings(4)
print('------------------------------------')
generate_diamond_arithmetic(4)
