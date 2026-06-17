# damit wir alle Funktionen von pygame abgreifen können, z. B.:
# - Fenster erstellen
# - Tastatur erkennen / lesen (input)
# - Grafik zeichnen
# - Sound abspielen
# - Kollisionen erkennen
# - ...
import pygame

# um Programm später sauber zu beenden (reine Ressourcen-Gschicht!)
import sys

# JSON laden:
import json

# Spieler-Model verwenden!
# from "ordner.dateiname_ohne_endung import klassenname"
from models.player import Player
# Wall-Modell verwenden!
from models.wall import Wall

# pygame zunächst starten!
# also intern wichtige Systeme vorbereiten (Grafik, Tastatur, Sound, ..)
pygame.init()

# EINSTELLUNGEN FÜR SPIEL

# Fensterbreite
WIDTH = 800
# Fensterhöhe
HEIGHT = 600
# Fensterfarbe
BLACK = (0, 0, 0)

# Fenster erstellen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Fenstertitel setzen ("Dungeon Crawler")
pygame.display.set_caption("Dungeon Crawler")

# FPS CLOCK
# Clock hilft uns, die FPS zu kontrollieren!
clock = pygame.time.Clock()

# WÄNDE:
# Datei "dungeon.json" öffnen und in ein python dict umwandeln
with open("data/dungeon.json", "r") as file:
    dungeon_data = json.load(file)

walls = []
for wall_data in dungeon_data["walls"]:
    wall = Wall(
        x=wall_data["x"],
        y=wall_data["y"],
        width=wall_data["width"],
        height=wall_data["height"],
    )
    walls.append(wall)



# SPIELER:
player = Player()

# GAME LOOP VARIABLE (running)
running = True # wenn True, dann läuft Spiel!

# GAME LOOP (= Herzstück unseres Spiel!)
# solange running True ist, läuft Spiel permanent weiter!

while running:

    # EVENTS VERARBEITEN

    # pygame fragen, ob was passiert ist (z. B. Taste gedrückt, etc.)
    
    # for = für "jedes" Event!!!
    for event in pygame.event.get():
        
        # Event, dass man immer abfragen muss: "Wurde das Fenster geschlossen?"
        if event.type == pygame.QUIT:
            
            # Spiel stoppen.
            running = False
    
    keys = pygame.key.get_pressed() # liefert uns entsprechenden Zustand der Tasten

    old_x = player.rect.x
    old_y = player.rect.y

    player.move(keys)

    for wall in walls:
        if player.rect.colliderect(wall.rect):
            player.rect.x = old_x
            player.rect.y = old_y

    player.stay_in_bounds(
        screen.get_rect()
    )


    # SPIEL SAUBER ZEICHNEN (HINTERGRUND)

    screen.fill(BLACK) # RGB-Farben!

    # zeichnet uns ein Rechteck (Quadrat)

    for wall in walls:
        wall.draw(screen)

    player.draw(screen)

    pygame.display.update() # ohne diese Zeile würde nichts erscheinen!

    # FPS BEGRENZEN
    # max. 60 Bilder pro Sekunde, damit Spiel flüssig und stabil läuft
    # UND: v. a. auf verschiedenen PCS ähnlich!
    clock.tick(60)

# SPIEL SAUBER BEENDEN (in 2 Schritten)

# 1. pygame herunterfahren
pygame.quit()

# 2. Python-Pgrogramm selbst sauber schließen
sys.exit()