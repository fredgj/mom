from functools import wraps

def decorators(*decorators):
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

