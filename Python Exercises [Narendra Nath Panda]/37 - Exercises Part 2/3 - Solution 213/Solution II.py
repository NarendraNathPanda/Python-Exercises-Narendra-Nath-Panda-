from itertools import groupby


def compress(number):
    result = [''.join((key, str(len(list(group))))) for key, group in groupby(str(number))]
    return '_'.join(result)