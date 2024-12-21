import pyautogui
import random
import time

# Funzione per ottenere la risoluzione dello schermo
def get_screen_size():
    screen_width, screen_height = pyautogui.size()
    return screen_width, screen_height

# Funzione per muovere il mouse con variazione casuale
def move_mouse_with_variation(x, y):
    x_variation = random.randint(-10, 10)  # variazione casuale
    y_variation = random.randint(-10, 10)
    pyautogui.moveTo(x + x_variation, y + y_variation)
    time.sleep(random.uniform(0.3, 1.0))  # Ritardo casuale

# Funzione per cliccare in una posizione specifica
def click_at(x, y):
    move_mouse_with_variation(x, y)
    pyautogui.click()

# Funzione per scrivere del testo
def write_text(text):
    pyautogui.typewrite(text, interval=random.uniform(0.1, 0.3))  # Scrittura con intervallo casuale

# Funzione per premere un tasto
def press_key(key):
    pyautogui.press(key)
    time.sleep(random.uniform(0.2, 0.5))  # Ritardo casuale
import cv2
import numpy as np

# Funzione per trovare un'icona e cliccare su di essa
def locate_and_click_image(image_path):
    try:
        screenshot = pyautogui.screenshot()
        screenshot_gray = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2GRAY)

        template = cv2.imread(image_path, 0)
        result = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        
        if max_val > 0.8:  # soglia di confidenza
            print(f"Immagine trovata a {max_loc}")
            click_at(max_loc[0], max_loc[1])
        else:
            print("Immagine non trovata")
    except Exception as e:
        print(f"Errore nel trovare l'immagine: {e}")
# Esempio di simulazione di apertura dell'inventario e selezione di un blocco
def open_inventory_and_select_block(inventory_icon_path, block_icon_path):
    # Clicca sull'icona dell'inventario
    locate_and_click_image(inventory_icon_path)
    
    # Dopo aver aperto l'inventario, seleziona un blocco
    locate_and_click_image(block_icon_path)
    
# Esegui l'azione di costruzione
def build_block(x, y):
    # Muove e clicca nella posizione per costruire
    move_mouse_with_variation(x, y)
    pyautogui.click()
# Funzione per saltare in Minecraft (o altri giochi)
def jump():
    press_key('space')  # Spazio per saltare in Minecraft

# Funzione per attaccare un nemico
def attack():
    press_key('left')  # Tasto sinistro per attaccare in alcuni giochi
def play_game():
    # Esegui alcune azioni: movimenti casuali, attacco, costruzione
    move_mouse_with_variation(500, 300)  # Esempio di movimento
    jump()  # Esegui il salto
    build_block(600, 400)  # Costruisci un blocco in una posizione
    attack()  # Attacca un nemico

# Avvia il gioco
play_game()
