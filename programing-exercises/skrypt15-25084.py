def collect_divisible():
    liczby = []
    for i in range(1, 101):
        if i % 3 == 0 or i % 5 == 0:
            liczby.append(i)
    print(liczby)

if __name__ == '__main__':
    collect_divisible()
