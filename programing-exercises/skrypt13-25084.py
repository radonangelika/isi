def skip_multiples_of_3():
    # Iterujemy po liczbach od 1 do 50
    for i in range(1, 51):
        # Sprawdzamy, czy liczba nie jest podzielna przez 3
        if i % 3 != 0:
            # Wypisujemy liczbę, oddzielając je spacją (bez nowej linii)
            print(i, end=' ')

if __name__ == '__main__':
    skip_multiples_of_3()
