def find_substring():
    # Pobieramy od użytkownika tekst, w którym będziemy szukać
    tekst = input("Podaj tekst: ")
    # Pobieramy ciąg znaków, którego będziemy szukać w tekście
    szukany = input("Podaj ciąg do wyszukania: ")
    # Metoda find() zwraca indeks pierwszego wystąpienia szukanego ciągu lub -1, jeśli go nie ma
    print(tekst.find(szukany))  # -1 jeśli brak

if __name__ == '__main__':
    find_substring()
