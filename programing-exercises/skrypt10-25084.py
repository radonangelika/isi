def generate_and_save_alphabet():
    # Tworzymy ciąg znaków zawierający litery od 'a' do 'z'
    alphabet = ''.join([chr(i) for i in range(ord('a'), ord('z') + 1)])

    # Otwieramy plik alfabet1-25084.txt w trybie zapisu i zapisujemy cały alfabet jako jeden ciąg znaków
    with open("alfabet1-25084.txt", "w") as f1:
        f1.write(alphabet)

    # Otwieramy plik alfabet2-25084.txt w trybie zapisu i zapisujemy każdą literę w nowej linii
    with open("alfabet2-25084.txt", "w") as f2:
        for litera in alphabet:
            f2.write(litera + "\n")

if __name__ == '__main__':
    generate_and_save_alphabet()
