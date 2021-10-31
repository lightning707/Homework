from functools import wraps


class TypeDecorators:

    @staticmethod
    def to_int(func):
        """Convert to int"""
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return int(func(*args, **kwargs))
            except ValueError:
                print("Impossible to convert to int")
        return wrapper

    @staticmethod
    def to_bool(func):
        """Convert to bool"""
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return bool(func(*args, **kwargs))
            except ValueError:
                print("Impossible to convert to bool")
        return wrapper

    @staticmethod
    def to_str(func):
        """Convert to str"""
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return str(func(*args, **kwargs))
            except ValueError:
                print("Impossible to convert to str")
        return wrapper

    @staticmethod
    def to_float(func):
        """Convert to float"""
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return float(func(*args, **kwargs))
            except ValueError:
                print("Impossible to convert to float")
        return wrapper


@TypeDecorators.to_int
def do_nothing(string: str):
    return string


@TypeDecorators.to_bool
def do_something(string: str):
    return string


@TypeDecorators.to_float    
def do_asdf(string: str):
    return string


assert do_nothing("25") == 25
print(do_nothing("a"))
assert do_something("True") is True
print(do_something(None))
print(do_something(0))
print(do_asdf("a"))
help(TypeDecorators.to_int)
