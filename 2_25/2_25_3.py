def multiply(a: int, n: int, res=0):
    if n < 0:
        raise ValueError("This function works only with positive integers")
    else:
        if n == 0:
            return res
        else:
            return multiply(a, n - 1, res + a)


print(multiply(2, 4))
print(multiply(3, 8))
print(multiply(2, 0))
