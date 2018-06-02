""" Apply a function to every item in an iterable, and returns a list of the results"""

# take a string of numbers and convert them to a list of integers"""
s = "1 2 3 4 5 6 7 8 9 10"
n = map(int, s.split())
print n
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]