class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def talk(self):
        print(f"Hello, my name is {self.firstname} {self.lastname} and I'm {self.age} years old.\n")

cj = Person("Carl", "Johnson", 26)
me = Person("Andrew", "Bortnik", 20)

cj.talk()
me.talk()
