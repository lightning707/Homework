def outer_func():
    def inner_func(a):
        print(a)
    return inner_func

outer_func()("Hello world")
