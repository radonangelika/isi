def divisible_by_3_and_4():
    count = 0
    for i in range(1, 101):
        if i % 3 == 0 and i % 4 == 0:
            print(i, end=' ')
            count += 1
    print(f"\nLiczba takich liczb: {count}")

if __name__ == '__main__':
    divisible_by_3_and_4()
