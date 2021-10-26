class Animal:
    def talk(self):
        raise NotImplementedError("Talk method not implemented")


class Dog(Animal):
    def talk(self):
        print("woof woof")


class Cat(Animal):
    def talk(self):
        print("meow")


def exec_talk(obj_animal):
    obj_animal.talk()


exec_talk(Dog())
exec_talk(Cat())
