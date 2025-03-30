liczby = []

for i in range(1,101):
    if i % 3 == 0 and i % 4 == 0:
        liczby.append(i)
        
print("Liczby podzielne przez 3 i 4", liczby)
print("ilość tych liczb", len(liczby))