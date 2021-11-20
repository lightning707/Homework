def reverse(input_str: str, res='') -> str:
    if len(input_str) == 0:
        return res
    else:
        return reverse(input_str[0:-1], res + input_str[-1])


print(reverse('hello'))
print(reverse('my name is Andrew'))
