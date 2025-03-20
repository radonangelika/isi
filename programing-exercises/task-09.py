from datetime import datetime

class Vehicle:
    def __init__(self, nazwa, rok_produkcji, przebieg):
        self.nazwa = nazwa
        self.rok_produkcji = rok_produkcji
        self.przebieg = przebieg
        
    @property
    def age(self):
        return datetime.now().year - self.rok_produkcji
    
    def is_old(self):
        return self.age > 10
    
    def is_long_mileage(self):
        return self.przebieg > 200000

class Car(Vehicle):
    def __init__(self, nazwa, rok_produkcji, przebieg, marka):
        super().__init__(nazwa, rok_produkcji, przebieg)
        self.marka = marka
    
    @property
    def in_thousands(self):
        return self.przebieg / 1000

    def is_old(self):
        return self.age > 5

vehicle1 = Vehicle("ford mustang", 1994, 300000)
car1 = Car("chrysler 300c", 2005, 172000, "chrysler")
car2 = Car("tesla S", 2017, 120000, "tesla")

print(f"Vehicle1 ({vehicle1.nazwa}):")
print(f"Jest stary? {vehicle1.is_old()}")
print(f"Ma duży przebieg? {vehicle1.is_long_mileage()}")
print(f"Wiek pojazdu: {vehicle1.age} lat\n")

print(f"Car1 ({car1.nazwa}):")
print(f"Jest stary? {car1.is_old()}")
print(f"Ma duży przebieg? {car1.is_long_mileage()}")
print(f"Przebieg w tysiącach km: {car1.in_thousands} tys.\n")

print(f"Car2 ({car2.nazwa}):")
print(f"Jest stary? {car2.is_old()}")
print(f"Ma duży przebieg? {car2.is_long_mileage()}")
print(f"Przebieg w tysiącach km: {car2.in_thousands} tys.")