correct_inp = False
while not correct_inp:
    name = input("Enter your name: ")
    if name.isalpha():
        correct_inp = True
        name = name.lower()
        name = name.capitalize()
    else:
        print("Incorrect input")

correct_inp = False
while not correct_inp:
    age = input("Enter your age: ")
    if age.isdecimal():
        correct_inp = True
        age = int(age)
    else:
        print("Incorrect input")

print(f"Hello {name}, on your next birthday you'll be {age + 1} years")
