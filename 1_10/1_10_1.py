def oops():
    raise IndexError


def call_oops():
    try:
        oops()
    except IndexError:
        print("IndexError exception")


call_oops()
