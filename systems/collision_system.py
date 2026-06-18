class CollisionSystem:

    # Methode soll auch ohne Instanz zugänglich sein!
    @staticmethod
    def resolve_entity_walls(entity, walls, old_x, old_y):
        for wall in walls:
            if entity.rect.colliderect(wall.rect):
                entity.rect.x = old_x
                entity.rect.y = old_y