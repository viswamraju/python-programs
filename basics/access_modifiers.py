class Student:
    schoolName = 'XYZ School' # class attribute

    def __init__(self, name, age):
        self.name=name # instance attribute
        self.age=age # instance attribute


class Student1:
    _schoolName = 'XYZ School'  # protected class attribute

    def __init__(self, name, age):
        self._name = name  # protected instance attribute
        self._age = age  # protected instance attribute


class Student3:
    __schoolName = 'XYZ School' # private class attribute

    def __init__(self, name, age):
        self.__name=name  # private instance attribute
        self.__salary=age # private instance attribute

    def __display(self):  # private method
        print('This is private method.')

std = Student3('Viswam', 29)
print(std._Student3__name)

