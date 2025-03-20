tekst = input("Podaj łańcuch znakowy: ")
szukany_ciag = input("Podaj ciąg, którego szukasz: ")


czesci = tekst.split(szukany_ciag)


if len(czesci) == 1:
    print("-1 (ciąg nie został znaleziony)")
else:
    indeksy = []
    pozycja = 0

   
    for czesc in czesci[:-1]:
        pozycja += len(czesc)
        indeksy.append(pozycja)
        pozycja += len(szukany_ciag) 
    print(f"Indeksy wystąpień ciągu: {indeksy}")