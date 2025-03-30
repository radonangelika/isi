class Dog:
    def __init__(self, name, age, coat_color):
        """Konstruktor klasy Dog"""
        self.name = name
        self.age = age
        self.coat_color = coat_color
        
    def sound(self):
        """Metoda wypisujaca dzwiek"""
        print(f"{self.name} is barking")
        
    #tworzenie obiektów klsy Dog
dog1 = Dog("Azor", 3, "Brown")
dog2 = Dog("Reksio", 5, "Black")
dog3 = Dog("Puszek", 8, "Yellow")
    
dog1.sound()
dog2.sound()
dog3.sound()
    
    # Dodatkowe informacje o psach
print(f"{dog1.name} ma {dog1.age} lata i jest koloru {dog1.coat_color}.")
print(f"{dog2.name} ma {dog2.age} lata i jest koloru {dog2.coat_color}.")
print(f"{dog3.name} ma {dog3.age} lata i jest koloru {dog3.coat_color}.")