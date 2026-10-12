# class with an __init__() constructor and a method
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)


# create an object and call its method
p1 = Person("John", 36)
p1.myfunc()
