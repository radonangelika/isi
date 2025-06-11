def find_all_occurrences():
    # Pobieramy od użytkownika tekst, w którym będziemy szukać
    tekst = input("Podaj tekst: ")
    # Pobieramy ciąg znaków, którego będziemy szukać
    szukany = input("Podaj ciąg do wyszukania: ")
    # Lista do przechowywania indeksów znalezionych wystąpień
    indeksy = []

    # Szukamy pierwszego wystąpienia szukanego ciągu w tekście
    i = tekst.find(szukany)
    # Pętla działa dopóki znajdziemy kolejne wystąpienia (find zwraca -1 gdy brak)
    while i != -1:
        indeksy.append(i)  # dodajemy indeks do listy
        # Szukamy kolejnego wystąpienia, zaczynając od pozycji po ostatnio znalezionym indeksie
        i = tekst.find(szukany, i + 1)

    # Jeśli lista indeksów nie jest pusta, wypisujemy ją, w przeciwnym wypadku -1
    print(indeksy if indeksy else -1)

if __name__ == '__main__':
    find_all_occurrences()
