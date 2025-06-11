import random

def guess_game():
    # Losujemy sekretna liczbę z zakresu 1-100
    secret = random.randint(1, 100)
    while True:
        # Pobieramy od użytkownika zgadywaną liczbę
        guess = int(input("Zgadnij liczbę (1-100): "))
        # Sprawdzamy, czy zgadywana liczba jest równa sekretnej
        if guess == secret:
            print("Brawo! Zgadłeś!")
            break  # Kończymy pętlę, bo zgadnięto
        elif guess < secret:
            print("Za mało!")
        else:
            print("Za dużo!")

if __name__ == '__main__':
    guess_game()
