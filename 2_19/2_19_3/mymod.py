def is_filename(name):
    if type(name) != str:
        return False
    try:
        open(name)
    except FileNotFoundError:
        return False
    return True


def count_lines(name):
    if is_filename(name):
        with open(name, 'r') as file:
            return len(file.readlines())
    else:
        raise FileNotFoundError


def count_chars(name):
    if is_filename(name):
        with open(name, 'r') as file:
            return len(file.read())
    else:
        raise FileNotFoundError


def test(name):
    if is_filename(name):
        lines = count_lines(name)
        chars = count_chars(name)
        return lines, chars
    else:
        raise FileNotFoundErrorFileNotFoundError

