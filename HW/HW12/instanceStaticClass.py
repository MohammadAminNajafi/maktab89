# it is just practice
import datetime


class Person:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def show(self):
        return f'{self.name} is {self.height} cm and is {self.age} years old'

    @classmethod
    def from_birth(cls, name, height, age):
        return cls(name, height, datetime.datetime.now().year - age)


result = Person.from_birth('PEAMAN', 185, 2003).show()
print(result)