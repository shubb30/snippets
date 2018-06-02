""" Queue creates a FIFO (first in first out) queue that appends on the right, but pops
from the left
"""
from Queue import Queue

q = Queue()
q.put(1)
q.put(2)

print q.get()
# 1

print q.get()
# 2


""" LifoQueue allows you to create a queue that is appended, and popped from the right
side only
"""

from Queue import LifoQueue

q = LifoQueue()

q.put(1)
q.put(2)

print q.get()
# 2

print q.get()
# 1


""" PriorityQueue allows you to add a priority value to the work so that entries with
a higher priority will be retrieved first.

All objects entered into the priority queue need to have a __cmp__ method that can be
used to compare its priority to another object's priority.
"""

from Queue import PriorityQueue


class WorkItem(object):
	def __init__(self, pri, msg):
		self.priority = pri
		self.msg = msg

	def __cmp__(self, obj):
		return cmp(self.priority, obj.priority)

pq = PriorityQueue()

pq.put(WorkItem(1, "High priority job 1"))
pq.put(WorkItem(2, "Medium priority job 1"))
pq.put(WorkItem(2, "Medium priority job 2"))
pq.put(WorkItem(1, "High priority job 2"))
pq.put(WorkItem(3, "Low priority job 1"))
pq.put(WorkItem(3, "Low priority job 2"))
pq.put(WorkItem(2, "Medium priority job 3"))
pq.put(WorkItem(3, "Low priority job 3"))
pq.put(WorkItem(1, "High priority job 3"))
pq.put(WorkItem(3, "Low priority job 4"))
pq.put(WorkItem(1, "High priority job 4"))

while not pq.empty():
	work = pq.get()
	print work.msg

# High priority job 1
# High priority job 2
# High priority job 4
# High priority job 3
# Medium priority job 2
# Medium priority job 3
# Medium priority job 1
# Low priority job 2
# Low priority job 1
# Low priority job 4
# Low priority job 3
