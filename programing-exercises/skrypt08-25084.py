import random
import string
from collections import Counter

def analyze_random_string():
    # Generujemy losowy ciąg 100 znaków z liter (małych i wielkich) oraz cyfr
    ciag = ''.join(random.choices(string.ascii_letters + string.digits, k=100))
    # Tworzymy licznik wystąpień poszczególnych znaków w ciągu
    licznik = Counter(ciag)
    # Wypisujemy obiekt Counter z podsumowaniem wystąpień znaków
    print(licznik)

    # Zamieniamy licznik na listę krotek (znak, liczba_wystąpień)
    lista = list(licznik.items())
    # Wypisujemy tę listę
    print(lista)

if __name__ == '__main__':
    analyze_random_string()
