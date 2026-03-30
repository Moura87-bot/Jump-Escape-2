from code.Enemy import Enemy
from code.Entity import Entity


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Enemy):
            if ent.rect.right < 0:
                ent.health = 0

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for ent in entity_list:
            EntityMediator.__verify_collision_window(ent)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        # cria nova lista sem mortos
        entity_list[:] = [ent for ent in entity_list if ent.health > 0]