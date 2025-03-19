def sprawdz_liczbe(wejscie):
    if len(wejscie) < 2:
        return "Łańcuch musi mieć co najmniej dwa znaki."
    
    if all(char.isdigit() for char in wejscie):
        return "To jest liczba."
    else:
        return "To nie jest liczbą."
wejscie = input("Podaj łańcuch znaków: ")
print(sprawdz_liczbe(wejscie))
    