numer_albumu = "25084"


alfabet = ''.join([chr(i) for i in range(97, 123)])  # 'a' to 'z' ma kody ASCII od 97 do 122

plik1 = f"alfabet1-{numer_albumu}.txt"
with open(plik1, "w") as f1:
    f1.write(alfabet)

plik2 = f"alfabet2-{numer_albumu}.txt"
with open(plik2, "w") as f2:
    for litera in alfabet:
        f2.write(litera + "\n")

print(f"Alfabet zapisany do plików {plik1} i {plik2}.")