input_str = input("Input a phone number: ")

if not input_str.isdigit():
    print("Phone number should only contain numbers from 0 to 9")
elif len(input_str) != 10:
    print("Phone number length should be equal 10")
else:
    print(f"This is a correct phone number: {input_str}")
