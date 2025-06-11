class Vehicle:
    def __init__(self, nazwa, rok_produkcji, przebieg):
        # Konstruktor klasy Vehicle inicjujący nazwę, rok produkcji i przebieg pojazdu
        self.nazwa = nazwa
        self.rok_produkcji = rok_produkcji
        self.przebieg = przebieg

    @property
    def is_old(self):
        # Właściwość zwracająca True, jeśli pojazd jest starszy niż 10 lat (zakładamy rok 2025)
        return 2025 - self.rok_produkcji > 10

    @property
    def is_long_mileage(self):
        # Właściwość zwracająca True, jeśli przebieg pojazdu przekracza 200 000 km
        return self.przebieg > 200000

class Car(Vehicle):
    def __init__(self, nazwa, rok_produkcji, przebieg):
        # Konstruktor klasy Car wywołujący konstruktor klasy bazowej Vehicle
        super().__init__(nazwa, rok_produkcji, przebieg)

if __name__ == '__main__':
    # Tworzymy obiekt Vehicle i obiekt Car
    v = Vehicle("Fiat", 2008, 250000)
    c = Car("Audi", 2019, 120000)

    # Wyświetlamy informacje o tym, czy pojazdy są stare i czy mają duży przebieg
    print(f"{v.nazwa} - stary? {v.is_old}, duży przebieg? {v.is_long_mileage}")
    print(f"{c.nazwa} - stary? {c.is_old}, duży przebieg? {c.is_long_mileage}")
