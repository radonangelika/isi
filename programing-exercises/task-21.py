class Animal:
    """Klasa bazowa dla zwierząt"""
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def sound(self):
        """Metoda dźwięku (do nadpisania w klasach pochodnych)"""
        return "???"

    def info(self):
        """Zwraca podstawowe informacje o zwierzęciu"""
        return f"{self.name}, {self.age} lat(a), płeć: {self.sex}"


class Dog(Animal):
    """Klasa psa dziedzicząca po Animal"""
    def __init__(self, name, age, sex, breed):
        super().__init__(name, age, sex)
        self.breed = breed

    def sound(self):
        return "Hał! Hał!"

    def info(self):
        return f"🐶 Pies {self.name} ({self.breed}), {self.age} lat(a), płeć: {self.sex}"


class Cat(Animal):
    """Klasa kota dziedzicząca po Animal"""
    def __init__(self, name, age, sex, breed):
        super().__init__(name, age, sex)
        self.breed = breed

    def sound(self):
        return "Miał! Miał!"

    def info(self):
        return f"🐱 Kot {self.name} ({self.breed}), {self.age} lat(a), płeć: {self.sex}"


class Fox(Animal):
    """Klasa lisa dziedzicząca po Animal"""
    def sound(self):
        return "Ring-ding-ding-ding"  

    def info(self):
        return f"🦊 Lis {self.name}, {self.age} lat(a), płeć: {self.sex}"


# Tworzenie obiektów
dog = Dog("Reksio", 5, "samiec", "Labrador")
cat = Cat("Mruczek", 3, "samica", "Perski")
fox = Fox("Lisek", 2, "samiec")

# Wyświetlanie informacji i dźwięków
for animal in [dog, cat, fox]:
    print(animal.info())
    print(f"Dźwięk: {animal.sound()}\n")