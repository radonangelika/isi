def divisible_by_3_and_4():
    count = 0  # Zmienna do zliczania liczb podzielnych przez 3 i 4
    # Iterujemy po liczbach od 1 do 100
    for i in range(1, 101):
        # Sprawdzamy, czy liczba jest podzielna jednocześnie przez 3 i 4
        if i % 3 == 0 and i % 4 == 0:
            print(i, end=' ')  # Wypisujemy liczbę z odstępem
            count += 1         # Zwiększamy licznik
    # Po pętli wypisujemy ile takich liczb znaleźliśmy
    print(f"\nLiczba takich liczb: {count}")

if __name__ == '__main__':
    divisible_by_3_and_4()
