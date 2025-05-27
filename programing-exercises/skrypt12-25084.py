def zamien_znaki():
    tekst = input("Podaj zdanie: ")
    zamienione = tekst.replace("o", "0").replace("e", "3").replace("i", "1").replace("a", "4")
    print("Po zamianie:", zamienione)

if __name__ == '__main__':
    zamien_znaki()
