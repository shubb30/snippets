""" bisect.bisect allows you to very efficiently search for a value in a
sorted sequence.
"""
import bisect
import time
from random import randrange


def time_bisects(n):
	""" Bisect a 10 million long list n times"""
	numbers = range(10**7)  # 10 million numbers	
	t0 = time.time()
	i = 0
	while i < n:
		number = randrange(10**7)
		bisect.bisect(numbers, number)
		i += 1

	print "Bisected {} times in {} long list in {} seconds".format(
		n, len(numbers), time.time() - t0)


time_bisects(10000)
# Bisected 10000 times in 10000000 long list in 0.0242209434509 seconds

time_bisects(100000)
# Bisected 100000 times in 10000000 long list in 0.236649990082 seconds

time_bisects(1000000)
# Bisected 1000000 times in 10000000 long list in 2.20213198662 seconds


""" bisect.insort allows you to insert into a sorted list while keeping
the order.
"""

numbers = range(10**7)  # 10 million numbers	
t0 = time.time()
number = randrange(10**7)
bisect.insort(numbers, number)

print "Added entry in {} seconds".format(time.time() - t0)
# Added entry in 0.0031430721283 seconds

print "Section: {}".format(numbers[number-2:number+4])
# Section: [6259204, 6259205, 6259206, 6259206, 6259207, 6259208]
