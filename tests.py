import unittest
from mom import decorate


def decorator_without_args(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


def decorator_with_args(*args):
    def wrapper(func):
        def func_wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return func_wrapper
    return wrapper


@decorate(decorator_without_args, [decorator_with_args, 'arg1', 'arg2'])
def add(x,y):
    return x+y


class DecoratorsTest(unittest.TestCase):
    def test_add(self):
        return self.assertEqual(add(1,2), 3)


if __name__ == '__main__':
    unittest.main()

