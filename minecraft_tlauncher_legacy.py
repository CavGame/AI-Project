import subprocess
import time

def open_tlauncher_legacy():
    # Apre TLauncher Legacy (modifica il percorso in base alla tua installazione)
    launcher_path = "C:\\Path\\To\\TLauncherLegacy.exe"  # Modifica con il percorso corretto
    subprocess.Popen([launcher_path])
    time.sleep(5)  # Aspetta che TLauncher Legacy si carichi
import pyautogui

def select_tlauncher_legacy_version():
    # Clicca sul pulsante "Versioni" (modifica le coordinate in base al layout del launcher)
    pyautogui.click(x=500, y=300)  # Supponiamo che il pulsante "Versioni" sia a questa posizione
    time.sleep(1)

    # Seleziona la versione desiderata (modifica le coordinate in base alla tua versione di gioco)
    pyautogui.click(x=600, y=350)  # Clicca sulla versione 1.16.5 o quella desiderata
    time.sleep(1)
def press_play_button():
    # Clicca sul pulsante "Gioca" per avviare Minecraft
    pyautogui.click(x=700, y=400)  # Modifica con le coordinate esatte del pulsante "Gioca"
    print("Minecraft sta per partire...")
def wait_for_game_to_start():
    print("Aspettando che Minecraft si avvii...")
    time.sleep(30)  # Attendi circa 30 secondi per l'avvio
def start_building():
    # Esegui un'azione di costruzione, ad esempio cliccare per piazzare un blocco
    pyautogui.moveTo(600, 500)  # Posizione dove il blocco deve essere costruito
    pyautogui.click()
    print("Il blocco è stato costruito!")
def play_minecraft_legacy():
    # Passo 1: Apri TLauncher Legacy
    open_tlauncher_legacy()

    # Passo 2: Seleziona la versione
    select_tlauncher_legacy_version()

    # Passo 3: Premi il pulsante "Gioca"
    press_play_button()

    # Passo 4: Attendere che Minecraft si avvii
    wait_for_game_to_start()

    # Passo 5: Esegui le azioni di gioco (come costruire)
    start_building()

# Avvia il processo
play_minecraft_legacy()
