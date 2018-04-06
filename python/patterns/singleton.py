""" The Singleton pattern ensures that there is only ever
one instance of a class created at a time.  All instances of
the same Singleton class will be identical.

Any instances of sub-classes of a Singleton will be identical
to each other, but not identical to instances of another sub-class
of the Singleton

"""


class Singleton(object):
    def __new__(type):
        if not '_the_instance' in type.__dict__:
            type._the_instance = object.__new__(type)
        return type._the_instance


class Singleton1(Singleton):
    pass


class Singleton2(Singleton):
    pass


s01 = Singleton()
s02 = Singleton()

print "Are the Singleton object IDs the same? {}".format(id(s01) == id(s02))    # True

s11 = Singleton1()
s12 = Singleton1()

print "Are the Singleton1 object IDs the same? {}".format(id(s11) == id(s12))    # True

s21 = Singleton2()
s22 = Singleton2()

print "Are the Singleton2 object IDs the same? {}".format(id(s21) == id(s22))    # True

print "Are the Singleton and Singleton1 object IDs the same? {}".format(id(s01) == id(s11))    # False

print "Are the Singleton1 and Singleton2 object IDs the same? {}".format(id(s01) == id(s21))    # False
