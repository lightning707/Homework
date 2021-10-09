def make_operator(operator, *args):
    is_valid_inp = True
    for num in args:
        if (type(num) != int) and (type(num) != float):
            is_valid_inp = False
    if not is_valid_inp:
        print("Function parameters should contain only numbers")
        exit(1)
    expression = ''
    for num in args:
        if num != args[-1]:
            expression += str(num) + operator
        else:
            expression += str(num)
    result = eval(expression)
    print(result)


make_operator('+', -5, 3, 18, 33)
