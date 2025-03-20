import random
import string

numer_albumu = "25084"
nazwa_slownika = f"slownik_{numer_albumu}"


slownik = {}

for i in range(10, 21): 
    losowy_ciag = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    slownik[i] = losowy_ciag


print(f"Słownik {nazwa_slownika}:")
for klucz, wartosc in slownik.items():
    print(f"{klucz}: {wartosc}")