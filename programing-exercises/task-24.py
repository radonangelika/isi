import csv

def create_pc_csv(filename):
    """Tworzy plik CSV z komputerami i adresami IP"""
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["pc_name", "ip"])  # Nagłówek

        for i in range(1, 101):  # Zakres 1-100
            pc_name = f"P{i}"  # Nazwa komputera
            ip_address = f"172.30.2.{i}"  # Adres IP
            writer.writerow([pc_name, ip_address])  # Zapis do pliku

# Tworzenie pliku CSV
create_pc_csv("pc.csv")

print("Plik pc.csv został wygenerowany!")
