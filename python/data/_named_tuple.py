""" Sometimes it is useful to have an object that holds
key/value data and can be accessed by an attribute name
instead of using ['field'] from a dictionary

Named Tuples allow for this
"""

from collections import namedtuple

Person = namedtuple('Person', 'first last age sex address')
Address = namedtuple('Address', 'street city state country')

bob = Person('Bob', 'Smith', 30, 'M', Address('123 Main Street', 'Anytown', 'Anystate', 'USA'))

print bob
# Person(first='Bob', last='Smith', age=30, sex='M', address=Address(street='123 Main Street', city='Anytown', state='Anystate', country='USA'))


print bob.first, bob.last, bob.age, bob.sex
# Bob Smith 30 M

print bob.address
# Address(street='123 Main Street', city='Anytown', state='Anystate', country='USA')

print bob.address.state
# Anystate
