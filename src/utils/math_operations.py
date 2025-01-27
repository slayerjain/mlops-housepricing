def add_numbers(a, b):
    """
    Add two numbers.
    :param a: First number
    :param b: Second number
    :return: Sum of a and b
    """
    return a + b


def subtract_numbers(a, b):
    """
    Subtract the second number from the first number.
    :param a: First number
    :param b: Second number
    :return: Difference of a and b
    """
    return a - b


def multiply_numbers(a, b):
    """
    Multiply two numbers.
    :param a: First number
    :param b: Second number
    :return: Product of a and b
    """
    return a * b


def divide_numbers(a, b):
    """
    Divide the first number by the second number.
    :param a: First number
    :param b: Second number
    :return: Division of a by b
    :raises ZeroDivisionError: If b is zero
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b
