import requests
from bs4 import BeautifulSoup

def get_links(url):
    """Pobiera wszystkie linki ze strony"""
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Błąd pobierania strony!")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    links = [a["href"] for a in soup.find_all("a", href=True)]
    
    return links
url = "https://wp.pl"

# Pobieranie linków
links = get_links(url)

# Wyświetlenie wyników
print(f"Znaleziono {len(links)} linków:")
for link in links[:10]:  # Pokazuje pierwsze 10 linków
    print(link)