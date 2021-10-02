input_str = input("Input a string: ")

if len(input_str) < 2:
    print("")
else:
    print(input_str[:2] + input_str[-2:])
