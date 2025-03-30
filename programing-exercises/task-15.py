liczby = []

for i in range(1,101):
    if i % 3 == 0 or i % 5 == 0:
        liczby.append(i)
        
print("Liczby podzielne przez 3 i 5", liczby)
print("ilość tych liczb", len(liczby))