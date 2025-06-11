def collect_divisible():
    liczby = []  # Inicjalizujemy pustą listę do przechowywania liczb podzielnych przez 3 lub 5
    for i in range(1, 101):  # Przechodzimy przez liczby od 1 do 100
        if i % 3 == 0 or i % 5 == 0:  # Sprawdzamy, czy liczba jest podzielna przez 3 lub przez 5
            liczby.append(i)  # Jeśli tak, dodajemy ją do listy
    print(liczby)  # Wyświetlamy listę znalezionych liczb

if __name__ == '__main__':
    collect_divisible()
