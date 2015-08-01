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
their arguments and/or keyword arguments (if any), in order to apply them to a
function.

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

    # you can also add each decorator to a list if that's what you prefer,
    # like this:
    @decorate_with([decorator1],[decorator2], [decorator3, arg1, arg2])
    def func(*args, **kwargs):
        pass

As you can see in the example above, decorate_with takes other decorators as
arguments and applies them to the function. If the decorator has no arguments 
you can just pass it in directly, or as a list, it's up to the user. Though,
passing them in directly looks slightly more elegant.
If the decorator has any arguments you need to add it to a list together its 
arguments.


If a decorator has been defined with default arguments you need to pass the 
keyword arguments dictionary to decorate_with, in case you have any keyword
arguemnts to pass. 

First, lets write a simple decorator with two default arguments:
In the reality there are three default arguments, but **func** will be 
overwritten from wrapper inside the else part if **msg1** and/or **msg2** have a 
value.

.. code:: python
    
    def decorator(func=None, msg1=None, msg2=None):
        if func:
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)
            return wrapper
        else:
            def wrapper(func):
                def func_wrapper(*args, **kwargs):
                    if msg1:
                        print(msg1)
                    if msg2:
                        print(msg2)
                    return func(*args, **kwargs)
                return func_wrapper
            return wrapper

Now we can apply it like this:

.. code:: python

    @decorate_with([decorator, {'msg1':'hello', 'msg2':'world'}])
    def func(*args, **kwargs):
        pass

Or without any arguments        
    
.. code:: python

    @decorate_with(decorator)
    def func(*args, **kwargs):
        pass





