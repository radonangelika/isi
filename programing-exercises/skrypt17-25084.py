class Dog:
    def __init__(self, name, age, coat_color):
        # Konstruktor klasy Dog inicjujący imię, wiek i kolor sierści psa
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def sound(self):
        # Metoda wypisująca informację o szczekaniu psa
        print(f"{self.name} is barking!")

if __name__ == '__main__':
    # Tworzymy trzy obiekty klasy Dog z różnymi parametrami
    d1 = Dog("Max", 3, "brown")
    d2 = Dog("Luna", 2, "black")
    d3 = Dog("Buddy", 5, "white")

    # Iterujemy przez psy i wywołujemy ich metodę sound()
    for d in (d1, d2, d3):
        d.sound()
