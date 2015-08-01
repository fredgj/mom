Mom
===

Mom is a python module that contains one single decorator called decorate_with, 
but this is also a powerful decorator. It's the mother of all decorators.

In the future I might add some more meta stuff here, but at the moment I only 
need this single decorator.

It might not be the most useful decorator, but it intends to solve a problem,
at least for some people.


Usage
-----

decorate_with is a decorator that takes other decorators as input, including 
their arguments (if any).

Some people think decorating their functions with several decorators like in 
the example below looks way too ugly.

.. code:: python

    @decorator1
    @decorator2
    @decoraror3(arg1, arg2)
    def func(*args, **kwargs):
        pass

decorate_with lets you decorate your functions with all the decorators you need 
in one single "decoration".

.. code:: python

    from mom import decorate_with

    @decorate_with(decorator1, decorator2, [decorator3, arg1, arg2])
    def func(*args, **kwargs):
        pass



As you can see in the example above, decorate_with takes other decorators as
arguments and applies them to the function. If the decorator has no arguments 
you can just pass it in directly. If the decorator has arguemnts you
need to add it to a list together its arguments.

