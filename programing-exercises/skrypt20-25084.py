import random

def guess_game():
    secret = random.randint(1, 100)
    while True:
        guess = int(input("Zgadnij liczbę (1-100): "))
        if guess == secret:
            print("Brawo! Zgadłeś!")
            break
        elif guess < secret:
            print("Za mało!")
        else:
            print("Za dużo!")

if __name__ == '__main__':
    guess_game()



