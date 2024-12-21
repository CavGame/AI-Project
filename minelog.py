import pyautogui
import time

# Impostare le credenziali per il login (nome utente, password)
username = "FanginoK0"
password = "ciambella90"
server_ip = "minecraftserver.example.com"

def login_minecraft():
    # Avvia il launcher di Minecraft
    pyautogui.hotkey('win', 'r')
    time.sleep(1)
    pyautogui.write('Minecraft Launcher')
    pyautogui.press('enter')
    time.sleep(5)
    
    # Inserisci il nome utente
    pyautogui.write(username)
    pyautogui.press('tab')  # Spostati sul campo password
    time.sleep(1)
    
    # Inserisci la password
    pyautogui.write(password)
    pyautogui.press('enter')
    time.sleep(10)  # Attendi il login

    # Selezioniamo il server
    pyautogui.write(server_ip)
    pyautogui.press('enter')
    time.sleep(10)

login_minecraft()
# Movimento in Minecraft
def muovi_avanti():
    pyautogui.press('w')  # Muovi in avanti
    time.sleep(1)

def gira_sinistra():
    pyautogui.press('a')  # Gira a sinistra
    time.sleep(1)

def gira_destra():
    pyautogui.press('d')  # Gira a destra
    time.sleep(1)

def cammina_indietro():
    pyautogui.press('s')  # Muovi indietro
    time.sleep(1)
# Costruzione (piazzamento di blocchi)
def costruisci():
    pyautogui.click(button='right')  # Clicca con il tasto destro del mouse per piazzare un blocco
    time.sleep(1)
# Raccolta (mining)
def raccogli():
    pyautogui.click(button='left')  # Clicca con il tasto sinistro per raccogliere blocchi
    time.sleep(1)
def test_ai():
    # Login e connessione
    login_minecraft()
    
    # Test di movimento
    print("AI si sta muovendo...")
    muovi_avanti()
    gira_sinistra()
    gira_destra()
    cammina_indietro()
    
    # Test di costruzione
    print("AI sta costruendo...")
    costruisci()
    
    # Test di raccolta
    print("AI sta raccogliendo...")
    raccogli()

# Esegui il test
test_ai()
