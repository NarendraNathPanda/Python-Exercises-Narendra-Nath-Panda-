from itertools import groupby


def compress(number):
    result = []
    for key, group in groupby(str(number)):
        result.append((key, len(list(group))))
    result = [''.join((i, '.' * j)) for i, j in result]
    return ''.join(result)