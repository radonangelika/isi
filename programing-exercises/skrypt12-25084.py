def zamien_znaki():
    # Pobieramy od użytkownika zdanie
    tekst = input("Podaj zdanie: ")
    # Zamieniamy litery na cyfry według zadanego wzoru:
    # 'o' na '0', 'e' na '3', 'i' na '1', 'a' na '4'
    zamienione = tekst.replace("o", "0").replace("e", "3").replace("i", "1").replace("a", "4")
    # Wypisujemy zmieniony ciąg znaków
    print("Po zamianie:", zamienione)

if __name__ == '__main__':
    zamien_znaki()
