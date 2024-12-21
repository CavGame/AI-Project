# main.py
import MinecraftJava
import BrawlStars
import ClashRoyale
import ClashOfClans
import SquadBuster
import Fortnite
import FallGuys
import StumbleGuys

def start_all_games():
    print("Avvio tutti i giochi...")
    
    # Avvia tutti i giochi uno dopo l'altro
    MinecraftJava.start_game()
    BrawlStars.start_game()
    ClashRoyale.start_game()
    ClashOfClans.start_game()
    SquadBuster.start_game()
    Fortnite.start_game()
    FallGuys.start_game()
    StumbleGuys.start_game()

    # Esegui altre azioni nel gioco (esempio di battaglie o round)
    MinecraftJava.collect_resources()
    BrawlStars.play_battle()
    ClashRoyale.play_battle()
    ClashOfClans.build_base()
    SquadBuster.play_game()
    Fortnite.perform_action()
    FallGuys.play_round()
    StumbleGuys.play_round()

# Avvio del processo
start_all_games()
