def najdluzszy_wyraz(plik):
    # Otwieramy plik w trybie do odczytu z kodowaniem UTF-8
    with open(plik, 'r', encoding='utf-8') as f:
        # Wczytujemy słowa - każda linia to jedno słowo, usuwamy białe znaki z końca/ początku
        slowa = [linia.strip() for linia in f]
    # Znajdujemy słowo o największej długości
    najdluzsze = max(slowa, key=len)
    # Wyświetlamy najdłuższe słowo oraz jego długość
    print(f"Najdłuższy wyraz: {najdluzsze} (długość: {len(najdluzsze)})")

def wyrazy_o_dlugosci_10(plik):
    # Otwieramy plik i wczytujemy słowa tak jak wyżej
    with open(plik, 'r', encoding='utf-8') as f:
        slowa = [linia.strip() for linia in f]
    # Filtrujemy słowa o długości dokładnie 10 znaków
    dziesiecioliterowe = [s for s in slowa if len(s) == 10]
    # Wyświetlamy liczbę takich słów
    print(f"Liczba wyrazów o długości 10: {len(dziesiecioliterowe)}")
    # Pokazujemy pierwsze 5 z nich jako przykład
    print("Przykładowe wyrazy:", dziesiecioliterowe[:5])

if __name__ == '__main__':
    plik = 'wordlist_10000.txt'  # Nazwa pliku do analizy
    najdluzszy_wyraz(plik)
    wyrazy_o_dlugosci_10(plik)
