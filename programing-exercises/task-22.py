def najdluzszy_wyraz(plik):
    with open(plik, "r", encoding="utf-8") as f:
        words = f.readlines()
    return max(words, key=len).strip()

def wyrazy_o_dl_10(plik):
    with open(plik, "r", encoding="utf-8") as f:
        words = f.readlines()
    return [word.strip() for word in words if len(word.strip()) == 10]

# Nazwa pliku
plik = "wordlist_10000.txt"

# Wyniki
print("Najdłuższy wyraz:", najdluzszy_wyraz(plik))
print("Wyrazy o długości 10 znaków:", wyrazy_o_dl_10(plik)[:5])