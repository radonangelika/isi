def is_palindrome():
    tekst = input("Podaj tekst: ").replace(" ", "").lower()
    print("To palindrom." if tekst == tekst[::-1] else "To NIE jest palindrom.")

if __name__ == '__main__':
    is_palindrome()
