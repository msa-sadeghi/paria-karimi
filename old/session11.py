class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"{self.name} is saying hello")

class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.grades = []
    def add_grade(self, score):
        self.grades.append(score)

    def average(self):
        return sum(self.grades) / len(self.grades)

class Teacher(Person):
    def __init__(self, name, age, level):
        super().__init__(name, age)
        self.level = level

    def exam(self):
        print(f"{self.name} is taking exam")



t1 = Teacher("ali", 37, 4)
t1.greet()
t1.exam()