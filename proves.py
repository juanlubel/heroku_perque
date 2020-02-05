#
#
# def hash_func(value):
#     hashed_key = 0
#     for i in value:
#         hashed_key += ord(i)
#
#     return hashed_key % 97
#
#
# Dict = {}
#
# elements = {
#     'juanlu': 'belda',
#     'juanlu2': 'belda2',
#     'juanlu3': 'belda3',
#     'juanlu4': 'belda4',
#     'juanlu5': 'belda5',
#
# }
#
#
# def test_for(elements):
#     for item in elements:
#         key = hash_func(item)
#         Dict[key] = {item: elements[item]}

import timeit


def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped


def test(n):
    L = []
    for i in range(n, 0):
        L.append(i)



number = 1000
wrapped = wrapper(test, number)

print(timeit.timeit(wrapped, number=1000000))
