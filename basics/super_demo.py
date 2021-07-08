class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def check(self):
        print("Person")


class Indian(Person):
    def __init__(self, name, age):
        super(Indian, self).__init__(name, age)

    def check(self):
        print("Indian")


class American(Person):
    def __init__(self, name, age):
        super(American, self).__init__(name, age)

    # def check(self):
    #     print("American")


class Student(American, Indian):
    def __init__(self, name, age, college):
        self.college = college
        super(American, self).__init__(name, age)

    # def check(self):
    #     print("Student")

a = Student("viswam", 18, "Narayana")
print(Student.mro())
a.check()
