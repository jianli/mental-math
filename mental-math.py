"""
Deliberately inefficient arithmetic using naive mental heuristics.

So far, only multiplication is implemented
"""

from __future__ import division

import itertools

multiplication_table = {}
for i, j in itertools.product(range(1, 13), range(1, 13)):
    multiplication_table[i, j] = i * j


def is_power_of_ten(x):
    """
    >>> is_power_of_ten(1)
    False
    >>> is_power_of_ten(3)
    False
    >>> is_power_of_ten(11)
    False
    >>> is_power_of_ten(100)
    True
    """
    return str(x)[0] == '1' and set(str(x)[1:]) == set('0')


def is_trailed_by_zeros(x):
    """
    >>> is_trailed_by_zeros(5)
    False
    >>> is_trailed_by_zeros(10)
    True
    """
    return True if (str(x)[-1] == '0') else False


def factor_trailing_zeros(x):
    """
    >>> factor_trailing_zeros(0)
    (0, 1)
    >>> factor_trailing_zeros(7)
    (7, 1)
    >>> factor_trailing_zeros(70)
    (7, 10)
    """
    str_x = str(x)
    zeros_so_far = 0
    for i in range(1, len(str_x)):
        if set(str_x[-i:]) == set('0'):
            zeros_so_far = i
        else:
            break
    zeros = zeros_so_far
    if zeros == 0:
        return x, 1
    else:
        return int(str_x[:-zeros]), int('1' + str_x[-zeros:])


def multiply_by_single_digit(number, single_digit):
    if len(str(single_digit)) != 1:
        raise ValueError('%d is not actually a single digit number' % number)
    result_accumulator = ''
    for position, numeral in enumerate(str(number)):
        product = multiplication_table[single_digit, int(numeral)]
        if position != 0 and len(str(product)) > 1:
            raise ValueError("The product is %d so I'd have to carry the %s" %
                             (product, str(product)[0]))
        result_accumulator += str(product)
    return int(result_accumulator)


def multiply(a, b):
    """
    >>> multiply(3, 111111111)
    Traceback (most recent call last):
      ...
    ValueError: Those numbers are too long for me to remember!
    >>> multiply(-1, -3)
    3
    >>> multiply(0, 88888)
    0
    >>> multiply(1, 88888)
    88888
    >>> multiply(6, 7)
    42
    >>> multiply(600, 1000)
    600000
    >>> multiply(20, 5)
    100
    >>> multiply(3, 222)
    666
    >>> multiply(33, 55)
    Traceback (most recent call last):
      ...
    ValueError: Could not calculate 33 * 55 in my head!
    """
    if len(str(a)) + len(str(b)) > 8:
        # See http://en.wikipedia.org/wiki/Digit_span
        raise ValueError('Those numbers are too long for me to remember!')

    # factor out negatives
    negatives = sum([x < 0 for x in (a, b)])
    if negatives:
        prefix = '-' if negatives % 2 != 0 else ''
        return int(prefix + str(multiply(abs(a), abs(b))))

    # multiply by 0
    if 0 in (a, b):
        return 0

    # multiply by 1
    if 1 in (a, b):
        return a if b == 1 else b

    # multiplication table lookup
    try:
        return multiplication_table[a, b]
    except KeyError:
        pass

    # multiplication by power of ten
    if any(map(is_power_of_ten, (a, b))):
        if is_power_of_ten(a):
            return int(str(b) + str(a)[1:])
        else:
            return int(str(a) + str(b)[1:])

    # factor trailing zeros
    if any(map(is_trailed_by_zeros, (a, b))):
        leading_a, trailing_a = factor_trailing_zeros(a)
        leading_b, trailing_b = factor_trailing_zeros(b)
        return multiply(
            multiply(leading_a, leading_b),
            multiply(trailing_a, trailing_b),
        )

    # multiply number by single digit number
    try:
        return multiply_by_single_digit(max(a, b), min(a, b))
    except ValueError:
        pass

    raise ValueError('Could not calculate %d * %d in my head!' % (a, b))


class NaiveNumber(int):
    def __init__(self, integer):
        self.integer = integer

    def __mul__(self, integer):
        return multiply(self.integer, integer)

    def __rmul__(self, integer):
        return multiply(self.integer, integer)

N = NaiveNumber

if __name__ == "__main__":
    import doctest
    doctest.testmod()
