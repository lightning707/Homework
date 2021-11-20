def is_palindrome(looking_str: str) -> bool:
    if len(looking_str) <= 1:
        return True
    else:
        if looking_str[-1] != looking_str[0]:
            return False
        else:
            return is_palindrome(looking_str[1:-1])


print(is_palindrome('aaabbbaaa'))
print(is_palindrome('123'))
print(is_palindrome('mom'))
print(is_palindrome('babab'))
print(is_palindrome('bebebeb'))
