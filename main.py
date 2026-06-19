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
# Display
from ui.hud import HUD
# Farb-Enums
from constants.colors import Colors
# Konstanten für Game Setting:
from constants.game_settings import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_SIZE, FPS, ENEMY_PATH, PLAYER_PATH

# pygame zunächst starten!
# also intern wichtige Systeme vorbereiten (Grafik, Tastatur, Sound, ..)
pygame.init()

# EINSTELLUNGEN FÜR SPIEL


# Fenster erstellen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

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
    width=PLAYER_SIZE,
    height=PLAYER_SIZE,
    color=Colors.GREEN.value,
    speed=5,
    hp=100
)
player.load_sprite(PLAYER_PATH)

hud = HUD()

# GEGNER:
creatures = [
    player
]

for enemy_data in dungeon_data["enemies"]:
    enemy = Enemy(
        x=enemy_data["x"],
        y=enemy_data["y"],
        color=Colors.RED.value,
        speed=2
    )
    enemy.load_sprite(ENEMY_PATH)
    creatures.append(enemy)
    enemy.add_observer(hud)

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

    #player.move(keys)

    CollisionSystem.resolve_entity_walls(
        player,
        walls,
        old_x,
        old_y
    )

    # enemy_1.update()
    # enemy_2.update()
    for creature in creatures:
        if hasattr(creature, "update"):
            old_x_ent = creature.rect.x
            old_y_ent = creature.rect.y
            creature.update(keys)
            CollisionSystem.resolve_entity_walls(
                creature,
                walls,
                old_x_ent,
                old_y_ent
            )

    dead_creatures = []

    for creature in creatures:
        if isinstance(creature, Enemy):
            if player.rect.colliderect(creature.rect):
                creature.take_damage(2)
                if creature.is_dead():
                    dead_creatures.append(creature)

    for dead_creature in dead_creatures:
        creatures.remove(dead_creature)

    for creature in creatures:
        creature.stay_in_bounds(
            screen.get_rect()
        )


    # SPIEL SAUBER ZEICHNEN (HINTERGRUND)

    screen.fill(Colors.BLACK.value) # RGB-Farben!

    # zeichnet uns ein Rechteck (Quadrat)

    for wall in walls:
        wall.draw(screen)

    # player.draw(screen)
    # enemy_1.draw(screen)
    # enemy_2.draw(screen)
    hud.draw(screen)

    for creature in creatures:
        creature.draw(screen)


    pygame.display.update() # ohne diese Zeile würde nichts erscheinen!

    # FPS BEGRENZEN
    # max. 60 Bilder pro Sekunde, damit Spiel flüssig und stabil läuft
    # UND: v. a. auf verschiedenen PCS ähnlich!
    clock.tick(FPS)

# SPIEL SAUBER BEENDEN (in 2 Schritten)
# 1. pygame herunterfahren
pygame.quit()

# 2. Python-Pgrogramm selbst sauber schließen
sys.exit()