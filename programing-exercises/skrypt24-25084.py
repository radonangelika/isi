import csv

def generuj_pc_csv(nazwa_pliku):
    with open(nazwa_pliku, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['pc_name', 'ip'])
        for i in range(1, 101):
            ip = f"172.30.2.{i}"
            pc_name = f"P{i}"
            writer.writerow([pc_name, ip])

if __name__ == '__main__':
    generuj_pc_csv('pc.csv')
