def to_power(x, exp: int, res=1):
    if exp < 0:
        raise ValueError("This function only works with exp > 0")
    else:
        if exp == 0:
            return res
        else:
            return to_power(x, exp - 1, res * x)


print(to_power(2, 3))
print(to_power(3.5, 2))
# print(to_power(2, -1))
