def sum_of_digits(digit_string: str, res=0) -> int:
    if len(digit_string) == 0:
        return res
    else:
        if not digit_string.isdigit():
            raise ValueError("Input string must be digit string")
        return sum_of_digits(digit_string[1:], res + int(digit_string[0]))


print(sum_of_digits('123456'))
print(sum_of_digits('111'))
print(sum_of_digits(''))
