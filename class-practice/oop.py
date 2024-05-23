#class  - blueprint for creating objects
#object - an instance of a class

class Person:
    #constructor is used to create an object
    #self allows you to have access to the object you create
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

#create an object using the constructor method

myPerson = Person("Jane Doe", 30, "Teacher")
print(myPerson.name)
print(myPerson.age)
