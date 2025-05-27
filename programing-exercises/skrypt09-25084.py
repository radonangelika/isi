class Vehicle:
    def __init__(self, nazwa, rok_produkcji, przebieg):
        self.nazwa = nazwa
        self.rok_produkcji = rok_produkcji
        self.przebieg = przebieg

    @property
    def is_old(self):
        return 2025 - self.rok_produkcji > 10

    @property
    def is_long_mileage(self):
        return self.przebieg > 200000

class Car(Vehicle):
    def __init__(self, nazwa, rok_produkcji, przebieg):
        super().__init__(nazwa, rok_produkcji, przebieg)

if __name__ == '__main__':
    v = Vehicle("Fiat", 2008, 250000)
    c = Car("Audi", 2019, 120000)

    print(f"{v.nazwa} - stary? {v.is_old}, duży przebieg? {v.is_long_mileage}")
    print(f"{c.nazwa} - stary? {c.is_old}, duży przebieg? {c.is_long_mileage}")
