import random

def zgadnij_liczba():
    liczba_do_odgadniecia = random.randint(1,100)
    proba = 0
    
    print("🔢 Witaj w grze 'Zgadnij liczbę'! 🔢")
    print("Zgadnij liczbę z przedziału od 1 do 100.")   

    while True:
        zgadnij = int(input("Podaj liczbę: "))
        proba +=1
    
        if zgadnij < liczba_do_odgadniecia:
            print("🔻 Twoja liczba jest za mała!")
        elif zgadnij > liczba_do_odgadniecia:
            print("🔺 Twoja liczba jest za duża!")
        else:
            print(f"Brawo! udało Ci się trafić -> {liczba_do_odgadniecia} w {proba} próbach")
            break # koniec gry
    
zgadnij_liczba();