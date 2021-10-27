def arg_rules(type_=str, max_length=15, contains=[]):
    def validate(func):
        def wrapper(*args):
            for arg in args:
                if type(arg) != type_:
                    return False
                if len(arg) > max_length:
                    return False
                for word in contains:
                    if word not in arg:
                        return False
            return func(*args)
        return wrapper
    return validate


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


# assert create_slogan('johndoe05@gmail.com') is False
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'
