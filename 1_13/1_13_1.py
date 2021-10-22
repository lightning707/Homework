class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age


class Teacher(Person):
    def __init__(self, firstname, lastname, age, salary, subject):
        Person.__init__(self, firstname, lastname, age)
        self.salary = salary
        self.subject = subject


class Student(Person):
    def __init__(self, firstname, lastname, age, class_, avg_grade):
        Person.__init__(self, firstname, lastname, age)
        self.class_ = class_
        self.avg_grade = avg_grade


foo = Teacher("Sebastian", "Duck", 30, 10000, "History")
bar = Student("Ivan", "Erohin", 16,  "10B", 10.5)
