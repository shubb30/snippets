""" The Borg pattern ensures that all instances of a Borg class
will have the same state.  Any instance attributes set in one instance
will be the same in any other instances.

Any classes that are sub-classes of a Borg class will also share the
same state, even though they are different classes and can have 
different methods.

"""

class Borg(object):
    _state = {}
    def __new__(cls, *p, **k):
        self = object.__new__(cls, *p, **k)
        self.__dict__ = cls._state
        return self

class Borg1(Borg):
    pass


class Borg2(Borg):
    pass


b = Borg()
b1 = Borg1()
b2 = Borg2()

print "Are the object IDs the same? {}".format(id(b) == id(b1))    # False

b.foo = "bar"
print "Are the states the same? {}".format(b.foo == b1.foo == b2.foo)     # True
