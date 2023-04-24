# (list comprehension):

from itertools import groupby


def compress(number):
    return [(key, len(list(group))) for key, group in groupby(str(number))]