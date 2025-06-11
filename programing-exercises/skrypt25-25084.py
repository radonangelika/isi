import requests
from bs4 import BeautifulSoup

def pobierz_linki(url):
    # Wysyłamy żądanie HTTP GET pod podany adres URL
    response = requests.get(url)
    # Parsujemy pobrany kod HTML strony za pomocą BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    # Znajdujemy wszystkie tagi <a> z atrybutem href i zbieramy ich wartości
    linki = [a['href'] for a in soup.find_all('a', href=True)]
    return linki

if __name__ == '__main__':
    url = input("Podaj adres URL: ")
    linki = pobierz_linki(url)
    print(f"Znaleziono {len(linki)} linków:")
    for link in linki:
        print(link)
