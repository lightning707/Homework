def stop_words(words: list):
    def replace_words(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            print(result)
            for word in words:
                result = result.replace(word, '*')
            print(result)
            return result
        return wrapper
    return replace_words


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


# print(create_slogan("Steve"))
assert create_slogan("Steve") == "Steve drinks * in his brand new *!"
