import random
import string
from collections import Counter

def analyze_random_string():
    ciag = ''.join(random.choices(string.ascii_letters + string.digits, k=100))
    licznik = Counter(ciag)
    print(licznik)

    lista = list(licznik.items())
    print(lista)

if __name__ == '__main__':
    analyze_random_string()
