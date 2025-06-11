def is_digit_check():
    # Pobieramy od użytkownika znak i bierzemy tylko pierwszy znak (indeks 0)
    znak = input("Podaj znak: ")[0]

    # Sprawdzamy, czy znak jest cyfrą za pomocą metody isdigit()
    print(f"Sposób 1 (isdigit): {znak.isdigit()}")

    # Sprawdzamy, czy znak jest typu string i czy należy do ciągu cyfr '0123456789'
    print(f"Sposób 2 (isinstance + in): {isinstance(znak, str) and znak in '0123456789'}")

# Jeśli ten plik jest uruchamiany bezpośrednio, wywołujemy funkcję is_digit_check()
if __name__ == '__main__':
    is_digit_check()
