from itertools import groupby


def compress(number):
    result = []
    for key, group in groupby(str(number)):
        result.append((key, len(list(group))))
    return result