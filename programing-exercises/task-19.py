def palindrom(tekst):
    czysty_tekst = "".join(tekst.lower().split())
    return czysty_tekst == czysty_tekst[::-1]

zdanie = input("Podaj słowo lub zdanie: ")

if palindrom(zdanie):
    print("to jest palidndrom")
else:
    print("to nie jest palindrom")
    