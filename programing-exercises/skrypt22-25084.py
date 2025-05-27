def najdluzszy_wyraz(plik):
    with open(plik, 'r', encoding='utf-8') as f:
        slowa = [linia.strip() for linia in f]
    najdluzsze = max(slowa, key=len)
    print(f"Najdłuższy wyraz: {najdluzsze} (długość: {len(najdluzsze)})")

def wyrazy_o_dlugosci_10(plik):
    with open(plik, 'r', encoding='utf-8') as f:
        slowa = [linia.strip() for linia in f]
    dziesiecioliterowe = [s for s in slowa if len(s) == 10]
    print(f"Liczba wyrazów o długości 10: {len(dziesiecioliterowe)}")
    print("Przykładowe wyrazy:", dziesiecioliterowe[:5])

if __name__ == '__main__':
    plik = 'wordlist_10000.txt'
    najdluzszy_wyraz(plik)
    wyrazy_o_dlugosci_10(plik)
