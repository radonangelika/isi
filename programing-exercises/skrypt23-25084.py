import random
import string

def generuj_hasla(liczba, dlugosc):
    # Zbiór znaków: małe i wielkie litery oraz cyfry
    znaki = string.ascii_letters + string.digits
    # Generujemy listę haseł: każde o podanej długości, liczba haseł zgodna z argumentem
    return [''.join(random.choices(znaki, k=dlugosc)) for _ in range(liczba)]

def zapisz_do_pliku(nazwa_pliku, hasla):
    # Otwieramy plik do zapisu (kodowanie UTF-8)
    with open(nazwa_pliku, 'w', encoding='utf-8') as f:
        # Zapisujemy każde hasło w osobnej linii
        for haslo in hasla:
            f.write(haslo + '\n')

if __name__ == '__main__':
    # Generujemy 1000 haseł, każde o długości 6 znaków
    hasla = generuj_hasla(1000, 6)
    # Zapisujemy wygenerowane hasła do pliku 'passwords.txt'
    zapisz_do_pliku('passwords.txt', hasla)
