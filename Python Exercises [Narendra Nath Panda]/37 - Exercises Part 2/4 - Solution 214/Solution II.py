#(list comprehension):

from itertools import groupby


def compress(number):
    result = [''.join((key, '.' * len(list(group)))) for key, group in groupby(str(number))]
    return ''.join(result)