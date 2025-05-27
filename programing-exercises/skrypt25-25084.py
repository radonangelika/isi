import requests
from bs4 import BeautifulSoup

def pobierz_linki(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    linki = [a['href'] for a in soup.find_all('a', href=True)]
    return linki

if __name__ == '__main__':
    url = input("Podaj adres URL: ")
    linki = pobierz_linki(url)
    print(f"Znaleziono {len(linki)} linków:")
    for link in linki:
        print(link)
