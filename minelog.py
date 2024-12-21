import pyautogui
import time
import subprocess
import os

# Impostazioni del server
server_ip = "IP_DEL_TUO_SERVER"  # Inserisci l'IP del tuo server
server_port = "25565"  # Porta del server (di default è 25565)
username = "FanginoK0"  # Nickname dell'AI
password = "ciambella90"  # Password dell'AI

# Funzione per lanciare il gioco e accedere al server
def start_minecraft():
    # Comando per avviare Minecraft con Legacy Launcher
    os.system('start java -Xmx2G -Xms1G -jar MinecraftLauncher.exe')  # Modifica con il percorso giusto
    time.sleep(5)  # Aspetta che Minecraft si avvii

    # Inserisci il login e la password automaticamente
    pyautogui.write(username)
    pyautogui.press('tab')  # Passa al campo della password
    pyautogui.write(password)
    pyautogui.press('enter')  # Premi invio per fare login
    time.sleep(10)  # Aspetta che Minecraft si carichi

    # Connetti al server
    pyautogui.write(f'{server_ip}:{server_port}')
    pyautogui.press('enter')  # Premi invio per connettersi al server

# Funzione per muoversi in avanti (con tasto W)
def move_forward():
    pyautogui.keyDown('w')
    time.sleep(1)
    pyautogui.keyUp('w')

# Funzione per saltare (con tasto SPACE)
def jump():
    pyautogui.press('space')

# Funzione per raccogliere (con tasto 1 - raccogliere item nella barra veloce)
def collect_item():
    pyautogui.press('1')

# Funzione per costruire (posizionare blocco con il tasto destro)
def build():
    pyautogui.mouseDown(button='right')
    time.sleep(0.1)
    pyautogui.mouseUp(button='right')

# Funzione per fermarsi (con tasto S)
def stop():
    pyautogui.keyDown('s')
    time.sleep(1)
    pyautogui.keyUp('s')

# Funzione per eseguire le azioni
def play_game():
    move_forward()
    time.sleep(2)
    jump()
    time.sleep(1)
    collect_item()
    time.sleep(1)
    build()
    time.sleep(1)
    stop()

# Avvia Minecraft, effettua il login, connetti al server e inizia a giocare
def main():
    start_minecraft()
    play_game()

# Esegui il programma
if __name__ == "__main__":
    main()
