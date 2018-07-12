import functools

# partial function to apply a callable with a set argument.
# create a function to multiply a number by 3
from operator import mul
triple = functools.partial(mul, 3)

print triple(5)      # prints 
# 15

# It can also take an arbitrary number of arguments or keyword arguments to make a 
# shortcut to a wrapper function
def func1(arg1, arg2, kwarg1=True, kwarg2=False):
    print "arg1: {}".format(arg1)
    print "arg2: {}".format(arg2)
    print "kwarg1: {}".format(kwarg1)
    print "kwarg2: {}".format(kwarg2)

func_it = functools.partial(func1, "one", "two")

func_it(kwarg1="yes", kwarg2="no")

# arg1: one
# arg2: two
# kwarg1: yes
# kwarg2: no


