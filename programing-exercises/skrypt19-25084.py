def is_palindrome():
    # Pobieramy tekst od użytkownika, usuwamy spacje i zmieniamy na małe litery
    tekst = input("Podaj tekst: ").replace(" ", "").lower()
    # Sprawdzamy, czy tekst jest taki sam czytany od tyłu
    print("To palindrom." if tekst == tekst[::-1] else "To NIE jest palindrom.")

if __name__ == '__main__':
    is_palindrome()
