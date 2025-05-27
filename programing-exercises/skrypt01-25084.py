def is_digit_check():
    znak = input("Podaj znak: ")[0]

    print(f"Sposób 1 (isdigit): {znak.isdigit()}")
    print(f"Sposób 2 (isinstance + in): {isinstance(znak, str) and znak in '0123456789'}")

if __name__ == '__main__':
    is_digit_check()