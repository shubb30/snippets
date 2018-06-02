""" collections.deque is a thread-safe double-ended queue that can be added to or popped
from either end very efficiently.

deque objects can be used to create a most recently used (MRU) cache
"""
from collections import deque
from random import randrange


q = deque(maxlen=10)

for i in range(1000):
	n = randrange(100)
	q.append(n)

print q
# deque([92, 66, 4, 72, 49, 38, 43, 67, 44, 9], maxlen=10)

q.append(999)

print q
# deque([66, 4, 72, 49, 38, 43, 67, 44, 9, 999], maxlen=10)

q.appendleft(-100)

print q
# deque([-100, 66, 4, 72, 49, 38, 43, 67, 44, 9], maxlen=10)

print q.pop()  # pop from the right
# 9

print q
# deque([-100, 66, 4, 72, 49, 38, 43, 67, 44], maxlen=10)

print q.popleft()
# -100

print q
# deque([66, 4, 72, 49, 38, 43, 67, 44], maxlen=10)
