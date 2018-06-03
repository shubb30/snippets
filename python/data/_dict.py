""" Dictionary comprehension allows you to create a dictionary using a single line"""

d = {i: str(i) for i in range(5)}

print d
# {0: '0', 1: '1', 2: '2', 3: '3', 4: '4'}

# Reverse the keys and values

d2 = {v: k for k, v in d.items()}

print d2
# {'1': 1, '0': 0, '3': 3, '2': 2, '4': 4}

""" With a dictionary, when you try to modify a key that does not exist, it will
return a KeyError
"""

d = {}
#d['foo'].append('bar')

# Traceback (most recent call last):
#   File "_dict.py", line 21, in <module>
#     d['foo'].append('bar')
# KeyError: 'foo'

""" collections.defaultdict allows you to set an automatic value for any key that
does not exist when it is accessed """

from collections import defaultdict

d = defaultdict(list)
print d
# defaultdict(<type 'list'>, {})

d['foo'].append('bar')
print d
# defaultdict(<type 'list'>, {'foo': ['bar']})

""" collections.OrderedDict is a dictionary-like object that keeps the order of the keys as they are created"""

d = {}
d['one'] = 1
d['two'] = 2
d['three'] = 3
d['foo'] = 'bar'
d['something'] = 'else'
print d
# {'something': 'else', 'foo': 'bar', 'three': 3, 'two': 2, 'one': 1}

from collections import OrderedDict
od = OrderedDict()
od['one'] = 1
od['two'] = 2
od['three'] = 3
od['foo'] = 'bar'
od['something'] = 'else'
print od
# OrderedDict([('one', 1), ('two', 2), ('three', 3), ('foo', 'bar'), ('something', 'else')])

""" collections.Counter is a simple object that counts the number of times an item is updated"""
from collections import Counter

c = Counter()
c.update('hello')
print c
# Counter({'l': 2, 'h': 1, 'e': 1, 'o': 1})

c.update('how are you today?')
print c
# Counter({'o': 4, ' ': 3, 'a': 2, 'e': 2, 'h': 2, 'l': 2, 'y': 2, 'd': 1, 'r': 1, 'u': 1, 't': 1, 'w': 1, '?': 1})
print c['h']
# 2
