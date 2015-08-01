
"""
Mom
---
Mom is a python module that contains one single decorator called decorate_with, 
but this is also a powerful decorator. It's the mother of all decorators.

decorate_with is a decorator that takes other decorators as input, including 
their arguments (if any).
It lets you decorate your functions with all the decorators you need 
in one single "decoration".

It might not be the most useful decorator, but it intends to solve a problem,
at least for some people.

usage:
    from mom import decorate_with

    @decorate_with(decorator1, decorator2, [decorator3, arg1, arg2])
    def func(*args, **kwargs):
        pass
    

    This is how it works if you want to use a decorator defined with
    default arguments, you need to pass in the keyword arguments dictionary.
    
    @decorate_with([decorator, {'arg1':'Hello', 'arg2':'World'}])
    def func(*args, **kwargs):
        pass
"""

__title__ = 'mom'
__version__ = '0.1.0'
__author__ = 'Fredrik Gjertsen'
__licence__ = 'MIT'
__copyright__ = 'Copyright 2015 Fredrik Gjertsen'


from mom.meta import decorate_with
