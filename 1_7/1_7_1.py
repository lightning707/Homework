import random

number = random.randint(1, 10)


is_guessed = False
while not is_guessed:
    inp = input("Guess a number from 1 to 10: ")
    if (inp.isdecimal() == False) or (int(inp) not in range(1, 11)):
        print("Invalid input")
    else:
        inp = int(inp)
        if inp < number:
            print("Number is greater")
        if inp > number:
            print("Number is smaller")
        if inp == number:
            is_guessed = True
            print("Correct!")

