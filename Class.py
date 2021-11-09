class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi I am {self.name}")


person1 = Person("Samuel")
print(person1.name)
person1.talk()


person2 = Person("Uchechukwu")
print(person2.name)

person3 = 2*3

print(isinstance(person3, Person))
