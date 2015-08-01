from functools import wraps

def decorate_with(*decorators):
    """decorate_with is a decorator that takes other decorators as input,
       including their arguments (if any), and applies the them to the function
       being decorated"""
    def wrapper(func):
        @wraps(func)
        def func_wrapper(*args, **kwargs):
            _func = func
            for decorator in decorators:
                if isinstance(decorator, list):
                    dec = decorator[0]
                    arguments = decorator[1:len(decorator)]
                    _func = dec(*arguments)(_func)
                else:
                    _func = decorator(_func)
            return _func(*args, **kwargs)
        return func_wrapper
    return wrapper

