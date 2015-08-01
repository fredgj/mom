Mom
===

Mom is a python module that contains one single decorator called decorate, 
but this is also a powerful decorator. It's every decorators mom.

In the future I might add more meta stuff here, but at the moment I just need 
this single decorator.

It might not be the most useful decorator, but it intends to solve a problem,
at least for some people.


Usage
-----

Decorate is a decorator that takes other decorators as input, including their
arguments.

Since some people think decorating their functions with several
decorators looks ugly like in the example below

.. code:: python

    @decorator1
    @decorator2
    @decoraror3(arg1, arg2)
    def func(*args, **kwargs):
        pass

decorate lets you decorate you function with all the decorators you need in one 
single "decoration".

.. code:: python

   @decorate(decorator1, decorator2, [decorator3, arg1, arg2])
   def func(*args, **kwargs):
       pass



As you can see in the example above, decorate takes other decorators as
arguments and applies them to the function. If the decorator has no arguments 
you can just pass it in directly. If the decorator has arguemnts you
need to add it to a list together its arguments.





