def skip_multiples_of_3():
    for i in range(1, 51):
        if i % 3 != 0:
            print(i, end=' ')

if __name__ == '__main__':
    skip_multiples_of_3()
