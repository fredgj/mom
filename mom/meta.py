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
                    # In case the user isn't careful enough
                    if len(decorator) > 1:
                        arguments = decorator[1:len(decorator)]
                        kwarguments = {}
                        if isinstance(arguments[-1], dict):
                            kwarguments = arguments[-1]
                            arguments = arguments[0:len(arguments)-1]
                        _func = dec(*arguments, **kwarguments)(_func)
                    else:
                        _func = dec(_func)
                else:
                    _func = decorator(_func)
            return _func(*args, **kwargs)
        return func_wrapper
    return wrapper

