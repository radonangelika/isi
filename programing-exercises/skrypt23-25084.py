import random
import string

def generuj_hasla(liczba, dlugosc):
    znaki = string.ascii_letters + string.digits
    return [''.join(random.choices(znaki, k=dlugosc)) for _ in range(liczba)]

def zapisz_do_pliku(nazwa_pliku, hasla):
    with open(nazwa_pliku, 'w', encoding='utf-8') as f:
        for haslo in hasla:
            f.write(haslo + '\n')

if __name__ == '__main__':
    hasla = generuj_hasla(1000, 6)
    zapisz_do_pliku('passwords.txt', hasla)
