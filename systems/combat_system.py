from models.enemy import Enemy

class CombatSystem:

    @staticmethod
    def handle_player_enemy_collisions(player, creatures):
        dead_creatures = []
        for creature in creatures:
            if isinstance(creature, Enemy):
                if player.rect.colliderect(creature.rect):
                    damage = CombatSystem.calculate_damage(
                        player,
                        creature
                    )
                    creature.take_damage(damage)
                    if creature.is_dead():
                        dead_creatures.append(creature)
        for dead_creature in dead_creatures:
            creatures.remove(dead_creature)

    @staticmethod
    def calculate_damage(attacker, defender):
        return 2