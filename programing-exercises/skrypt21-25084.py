class Animal:
    def __init__(self, name, age, sex):
        # Konstruktor klasy bazowej Animal inicjujący imię, wiek i płeć zwierzęcia
        self.name = name
        self.age = age
        self.sex = sex

    def sound(self):
        # Metoda domyślna wypisująca ogólny dźwięk
        print("Generic sound")

class Dog(Animal):
    def __init__(self, name, age, sex, breed):
        # Konstruktor klasy Dog wywołujący konstruktor klasy Animal i dodający rasę psa
        super().__init__(name, age, sex)
        self.breed = breed

    def sound(self):
        # Nadpisujemy metodę sound dla psa
        print("Woof!")

class Cat(Animal):
    def __init__(self, name, age, sex, breed):
        # Konstruktor klasy Cat wywołujący konstruktor klasy Animal i dodający rasę kota
        super().__init__(name, age, sex)
        self.breed = breed

    def sound(self):
        # Nadpisujemy metodę sound dla kota
        print("Meow!")

class Fox(Animal):
    def sound(self):
        # Nadpisujemy metodę sound dla lisa (nie ma rasy)
        print("Ring-ding")

if __name__ == '__main__':
    # Tworzymy obiekty psów, kota i lisa, a następnie wywołujemy ich metodę sound()
    Dog("Burek", 3, "M", "Labrador").sound()
    Cat("Mruczek", 2, "F", "Pers").sound()
    Fox("Lisek", 5, "M").sound()






