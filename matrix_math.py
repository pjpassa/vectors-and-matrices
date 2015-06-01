from itertools import zip_longest
import math


class ShapeException(Exception):
    pass


def shape(matrix):
    try:
        row_length = len(matrix[0])
    except TypeError:
        return (len(matrix), )
    return (len(matrix), row_length)


def shape_check(input1, input2):
    if shape(input1) != shape(input2):
        raise(ShapeException)


def dot(vector1, vector2):
    shape_check(vector1, vector2)
    return sum([x * y for x, y in zip_longest(vector1, vector2)])


def magnitude(vector):
    return math.sqrt(dot(vector, vector))


def vector_multiply(vector, scalar):
    return [scalar * x for x in vector]


def vector_add(vector1, vector2):
    shape_check(vector1, vector2)
    return [x + y for x, y in zip_longest(vector1, vector2)]


def vector_sub(vector1, vector2):
    return vector_add(vector1, vector_multiply(vector2, -1))


def vector_sum():
    pass


def vector_mean():
    pass


def matrix_row():
    pass


def matrix_col():
    pass


def matrix_scalar_multiply():
    pass


def matrix_vector_multiply():
    pass


def matrix_matrix_multiply():
    pass
