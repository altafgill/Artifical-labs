# class with an __init__() constructor
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# create an object and read its attributes
p1 = Person("John", 36)
print(p1.name)
print(p1.age)
