import random
import string
from collections import Counter

losowy_ciag = ''.join(random.choices(string.ascii_letters + string.digits, k=100))

print("losowy ciąg znaków: ")
print(losowy_ciag)

znaki_counter = Counter(losowy_ciag)
slownik_znakow = dict(znaki_counter)
lista_tupli = list(slownik_znakow.items())

print("\nSłownik znaków:")
print(slownik_znakow)

    
print("\nLista krotek: ")
print(lista_tupli)