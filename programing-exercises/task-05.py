import math

pierwisatki = [(i,math.sqrt(i)) for i in range(1,256) if i % 2 == 0]
for idx, (liczba,pierwiastek) in enumerate(pierwisatki, start=1):
    print(f"{idx}: √{liczba} = {pierwiastek}")