teskt = input("Podaj łańcuch znaków:")
szukany_ciag = input("Szukany ciąg: ")

i = teskt.find(szukany_ciag)

if i != -1:
    print(f"Ciąg znaleziony w indeksie: {i}")
else:
    print("-1 (ciąg nie znaleziony)")