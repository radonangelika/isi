import csv

def generuj_pc_csv(nazwa_pliku):
    # Otwieramy plik CSV do zapisu z odpowiednim kodowaniem i bez dodatkowych pustych linii
    with open(nazwa_pliku, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        # Zapisujemy nagłówki kolumn
        writer.writerow(['pc_name', 'ip'])
        # Tworzymy 100 wpisów komputerów z nazwami P1, P2, ... P100 i adresami IP w podsieci 172.30.2.x
        for i in range(1, 101):
            ip = f"172.30.2.{i}"
            pc_name = f"P{i}"
            writer.writerow([pc_name, ip])

if __name__ == '__main__':
    generuj_pc_csv('pc.csv')
