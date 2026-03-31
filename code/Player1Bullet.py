from code.Entity import Entity
from code.const import WIN_WIDTH, ENTITY_SPEED


class Player1Bullet(Entity):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.speed = ENTITY_SPEED.get(name, 8)
        print("TAMANHO DA BALA:", self.rect.width, self.rect.height)

    def move(self):
        self.rect.centerx += self.speed  # ✔️ correto

        if self.rect.left > WIN_WIDTH:
            self.health = 0