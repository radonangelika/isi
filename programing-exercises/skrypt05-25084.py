import math

def method1():
    print("Sposób 1 (math):")
    # Iterujemy po liczbach od 1 do 256 (włącznie)
    for i in range(1, 257):
        # Sprawdzamy, czy liczba jest parzysta
        if i % 2 == 0:
            # Wypisujemy pierwiastek kwadratowy z liczby i
            print(f"sqrt({i}) = {math.sqrt(i)}")

def method2():
    print("\nSposób 2 (list comprehension):")
    # Tworzymy listę pierwiastków kwadratowych z liczb parzystych od 2 do 256 (krokiem 2)
    wyniki = [math.sqrt(i) for i in range(2, 257, 2)]
    # Wypisujemy całą listę wyników
    print(wyniki)

if __name__ == '__main__':
    method1()
    method2()
