""" Decorators are used to add extra functionality to a function, either before or
    after the function.  It can optionally replace the function completely
"""

def deco(func):
    def wrapped(*args, **kwargs):
        print "before decorating function {}".format(func.__name__)
        ret = func(*args, **kwargs)
        print "after decorating function {}".format(func.__name__)
        return ret
    return wrapped

@deco
def func1(arg1, kw1='baz'):
    print "running func1"
    return arg1, kw1

print func1('foo', 'bar')

# before decorating function func1
# running func1
# after decorating function func1
# ('foo', 'bar')


""" You can also create a decorator that takes parameters by adding an
    additional function wrapper.
"""

def deco2(deco_arg):
    def inner(func):
        def wrapped(*args, **kwargs):
            print "decorator argument {}".format(deco_arg)
            print "before decorating function {}".format(func.__name__)
            ret = func(*args, **kwargs)
            print "after decorating function {}".format(func.__name__)
            return ret
        return wrapped
    return inner

@deco2("argument!")
def func2():
    print "running func2"


func2()
# decorator argument argument!
# before decorating function func2
# running func2
# after decorating function func2
