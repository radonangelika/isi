def reverse_sentence():
    # Pobieramy od użytkownika zdanie
    tekst = input("Podaj zdanie: ")
    # Wypisujemy zdanie odwrócone znak po znaku (od końca do początku)
    print("Odwrócone:", tekst[::-1])

if __name__ == '__main__':
    reverse_sentence()
