""" Sets are a collection of unique items.  An item can be added
many times, but it will only exist once in the set"""

s = set()

s.add(1)
s.add(2)
print s 
# set([1, 2])

for i in range(5):
    s.add(i)
print s
# set([0, 1, 2, 3, 4])

for i in range(10):
    s.add(i)
print s
# set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

""" You can compare two sets """

s1 = set([1, 2, 3, 4])
s2 = set([3, 4, 5, 6])

# get the union (elements in either set)
print s1 | s2
# set([1, 2, 3, 4, 5, 6])

# get the intersection (elements in both sets)
print s1 & s2
# set([3, 4])

# get the difference between 2 sets

print s1 - s2
# set([1, 2])

print s2 - s1
# set([5, 6])

""" Sets can be created using literals instead of calling set()"""

s1 = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

s2 = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

print s2
# set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

print s1 == s2
# True

""" This can also be used to create sets using comprehension """

s3 = {i for i in xrange(10)}

print s3 == s2 == s1
# True
