class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def sound(self):
        print(f"{self.name} is barking!")

if __name__ == '__main__':
    d1 = Dog("Max", 3, "brown")
    d2 = Dog("Luna", 2, "black")
    d3 = Dog("Buddy", 5, "white")

    for d in (d1, d2, d3):
        d.sound()
