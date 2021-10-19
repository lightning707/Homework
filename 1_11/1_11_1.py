def local_variables():
    a = 123
    b = 'ASD'
    c = True

print(local_variables.__code__.co_nlocals)
