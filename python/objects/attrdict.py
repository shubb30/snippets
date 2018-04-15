""" Libraries that can create objects from dictionaries or lists.
    Adapted from https://gist.github.com/mmerickel/ff4c6faf867d72c1f19c.
    Added __str__ and __repr__ methods.
"""
import collections


def wrap(value):
    """
    The top-level API for wrapping an arbitrary object.

    This only works for ``dict``, ``list`` and ``tuple`` types. If you want
    to wrap other types you may write your own ``wrap`` and pass ``wrapper=``
    to ``DictProxy`` and ``ListProxy``.

    """
    if isinstance(value, dict):
        return DictProxy(value)
    if isinstance(value, (tuple, list)):
        return ListProxy(value)
    return value


class DictProxy(collections.Mapping):
    """
    A proxy for a dictionary that allows attribute access to underlying keys.

    You may pass a custom ``wrapper`` to override the logic for wrapping
    various custom types.

    """
    def __init__(self, obj, wrapper=wrap):
        self.obj = obj
        self.wrapper = wrapper

    def __getitem__(self, key):
        return self.wrapper(self.obj[key])

    def __len__(self):
        return self.obj.__len__()

    def __iter__(self):
        return self.obj.__iter__()

    def __getattr__(self, key):
        try:
            return self.wrapper(getattr(self.obj, key))
        except AttributeError:
            try:
                return self[key]
            except KeyError:
                raise AttributeError(key)

    def __str__(self):
        return str(self.obj)

    def __repr__(self):
        return self.__str__()


class ListProxy(collections.Sequence):
    """
    A proxy for a list that allows for wrapping items.

    You may pass a custom ``wrapper`` to override the logic for wrapping
    various custom types.

    """
    def __init__(self, obj, wrapper=wrap):
        self.obj = obj
        self.wrapper = wrapper

    def __getitem__(self, key):
        return self.wrapper(self.obj[key])

    def __len__(self):
        return self.obj.__len__()

    def __str__(self):
        return str(self.obj)

    def __repr__(self):
        return self.__str__()
