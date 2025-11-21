from functools import wraps


def log_activity(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        model_name = args[0].__class__.__name__
        func_name = function.__name__
        print('model_name',model_name)
        print('func_name',func_name)
        result = function(*args, **kwargs)
        return result

    return wrapper



