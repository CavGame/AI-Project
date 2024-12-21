import pyautogui
import time

def get_server_list(file_path='server.txt'):
    """Legge una lista di server dal file server.txt."""
    try:
        with open(file_path, 'r') as file:
            servers = [line.strip() for line in file.readlines() if line.strip()]
            return servers
    except FileNotFoundError:
        print(f"File '{file_path}' non trovato.")
        return []

def choose_server(servers):
    """Permette all'utente di scegliere un server dalla lista."""
    print("Seleziona un server dalla lista:")
    for i, server in enumerate(servers, 1):
        print(f"{i}. {server}")
    
    while True:
        try:
            choice = int(input("Inserisci il numero del server: "))
            if 1 <= choice <= len(servers):
                return servers[choice - 1]
            else:
                print("Numero non valido. Riprova.")
        except ValueError:
            print("Inserisci un numero valido.")

def connect_to_server(server_ip):
    """Automatizza la connessione al server specificato."""
    if not server_ip:
        print("Nessun server specificato.")
        return

    # Avvia il launcher
    pyautogui.press('win')  # Premi il tasto Windows
    time.sleep(2)
    pyautogui.write('TLauncher')  # Scrivi il nome del launcher
    pyautogui.press('enter')
    time.sleep(10)  # Aspetta che si avvii il launcher

    # Inserisci l'IP del server
    print(f"Connessione al server {server_ip}...")
    pyautogui.write(server_ip)
    pyautogui.press('enter')

# Leggi la lista dei server e scegli
servers = get_server_list()
if servers:
    selected_server = choose_server(servers)
    connect_to_server(selected_server)
else:
    print("Nessun server trovato in 'server.txt'.")
