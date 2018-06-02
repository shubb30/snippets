""" Take a list of items, and return a new list with items removed that do not match the filter criteria"""


# remove numbers from a list that are not even
n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even = filter(lambda x: x % 2 == 0, n)

print even
# [2, 4, 6, 8, 10]
