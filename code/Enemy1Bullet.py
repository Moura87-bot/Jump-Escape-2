from code.Entity import Entity
from code.const import ENTITY_SPEED


class Enemy1Bullet(Entity):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.speed = ENTITY_SPEED.get(name, 5)

    def move(self):
        self.rect.x -= self.speed

        if self.rect.right < 0:
            self.health = 0