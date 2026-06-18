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
# Gegner
from models.enemy import Enemy
# Wall-Modell verwenden!
from models.wall import Wall
# Kollisions-System verwenden!
from systems.collision_system import CollisionSystem

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
GREEN = (0, 255, 0)
RED = (255, 0, 0)

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
player = Player(
    x=100,
    y=100,
    width=50,
    height=50,
    color=GREEN,
    speed=5
)

# GEGNER:
entities = [
    player
]

for enemy_data in dungeon_data["enemies"]:
    enemy = Enemy(
        x=enemy_data["x"],
        y=enemy_data["y"],
        color=RED,
        speed=2
    )
    entities.append(enemy)

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

    CollisionSystem.resolve_entity_walls(
        player,
        walls,
        old_x,
        old_y
    )

    # enemy_1.update()
    # enemy_2.update()
    for entity in entities:
        if hasattr(entity, "update"):
            old_x_ent = entity.rect.x
            old_y_ent = entity.rect.y
            entity.update()
            CollisionSystem.resolve_entity_walls(
                entity,
                walls,
                old_x_ent,
                old_y_ent
            )

    player.stay_in_bounds(
        screen.get_rect()
    )


    # SPIEL SAUBER ZEICHNEN (HINTERGRUND)

    screen.fill(BLACK) # RGB-Farben!

    # zeichnet uns ein Rechteck (Quadrat)

    for wall in walls:
        wall.draw(screen)

    # player.draw(screen)
    # enemy_1.draw(screen)
    # enemy_2.draw(screen)
    for entity in entities:
        entity.draw(screen)


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