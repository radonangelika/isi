import random
import string

def generate_dict():
    # Tworzymy słownik, gdzie klucze to liczby od 10 do 20 (włącznie),
    # a wartości to losowe 8-znakowe ciągi składające się z liter i cyfr
    wynik = {
        i: ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        for i in range(10, 21)
    }
    # Wypisujemy wygenerowany słownik
    print(wynik)

if __name__ == '__main__':
    generate_dict()
