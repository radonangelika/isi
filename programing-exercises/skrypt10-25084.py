def generate_and_save_alphabet():
    alphabet = ''.join([chr(i) for i in range(ord('a'), ord('z') + 1)])

    with open("alfabet1-25084.txt", "w") as f1:
        f1.write(alphabet)

    with open("alfabet2-25084.txt", "w") as f2:
        for litera in alphabet:
            f2.write(litera + "\n")

if __name__ == '__main__':
    generate_and_save_alphabet()
