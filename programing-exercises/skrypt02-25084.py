def is_number_string():
    s = input("Podaj ciąg znaków (min 2 znaki): ")
    if len(s) >= 2:
        print("To liczba." if all(ch.isdigit() for ch in s) else "To NIE jest liczba.")
    else:
        print("Za mało znaków.")

if __name__ == '__main__':
    is_number_string()