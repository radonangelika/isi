def find_all_occurrences():
    tekst = input("Podaj tekst: ")
    szukany = input("Podaj ciąg do wyszukania: ")
    indeksy = []

    i = tekst.find(szukany)
    while i != -1:
        indeksy.append(i)
        i = tekst.find(szukany, i + 1)

    print(indeksy if indeksy else -1)

if __name__ == '__main__':
    find_all_occurrences()