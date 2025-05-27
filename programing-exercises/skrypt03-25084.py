def find_substring():
    tekst = input("Podaj tekst: ")
    szukany = input("Podaj ciąg do wyszukania: ")
    print(tekst.find(szukany))  # -1 jeśli brak

if __name__ == '__main__':
    find_substring()
