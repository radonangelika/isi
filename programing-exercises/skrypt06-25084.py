import random
import string

def generate_dict():
    wynik = {
        i: ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        for i in range(10, 21)
    }
    print(wynik)

if __name__ == '__main__':
    generate_dict()
