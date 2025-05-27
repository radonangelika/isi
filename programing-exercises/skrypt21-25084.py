class Animal:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def sound(self):
        print("Generic sound")

class Dog(Animal):
    def __init__(self, name, age, sex, breed):
        super().__init__(name, age, sex)
        self.breed = breed

    def sound(self):
        print("Woof!")

class Cat(Animal):
    def __init__(self, name, age, sex, breed):
        super().__init__(name, age, sex)
        self.breed = breed

    def sound(self):
        print("Meow!")

class Fox(Animal):
    def sound(self):
        print("Ring-ding")

if __name__ == '__main__':
    Dog("Burek", 3, "M", "Labrador").sound()
    Cat("Mruczek", 2, "F", "Pers").sound()
    Fox("Lisek", 5, "M").sound()







