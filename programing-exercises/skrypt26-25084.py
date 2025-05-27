import requests
from bs4 import BeautifulSoup
import csv

class Home:
    def __init__(self, header_name, price, price_for_m2):
        self.header_name = header_name
        self.price = price
        self.price_for_m2 = price_for_m2

def pobierz_oferty(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    oferty = []

   
    for oferta in soup.find_all('article'):
        header = oferta.find('h2')
        cena = oferta.find('span', class_='css-1vr19r7')
        cena_m2 = oferta.find('span', class_='css-1kga39u')

        if header and cena and cena_m2:
            home = Home(header.get_text(strip=True), cena.get_text(strip=True), cena_m2.get_text(strip=True))
            oferty.append(home)

    return oferty

def zapisz_do_csv(oferty, nazwa_pliku):
    with open(nazwa_pliku, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['header_name', 'price', 'price_for_m2'])
        for home in oferty:
            writer.writerow([home.header_name, home.price, home.price_for_m2])

if __name__ == '__main__':
    url = 'https://www.otodom.pl/pl/wyniki/sprzedaz/mieszkanie/pomorskie/gdynia/gdynia/gdynia?priceMax=600000&viewType=listing'
    oferty = pobierz_oferty(url)
    zapisz_do_csv(oferty, 'home.csv')
    print(f"Zapisano {len(oferty)} ofert do pliku home.csv")
