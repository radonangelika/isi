def is_number_string():
    # Pobieramy od użytkownika ciąg znaków (oczekujemy co najmniej 2 znaki)
    s = input("Podaj ciąg znaków (min 2 znaki): ")

    # Sprawdzamy, czy długość ciągu jest co najmniej 2
    if len(s) >= 2:
        # Sprawdzamy, czy wszystkie znaki w ciągu są cyframi
        # Jeśli tak, wypisujemy "To liczba.", w przeciwnym razie "To NIE jest liczba."
        print("To liczba." if all(ch.isdigit() for ch in s) else "To NIE jest liczba.")
    else:
        # Informujemy użytkownika, że podany ciąg jest za krótki
        print("Za mało znaków.")

if __name__ == '__main__':
    is_number_string()
