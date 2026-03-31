import pygame

from code.Entity import Entity
from code.const import ENTITY_SPEED, WIN_WIDTH, WIN_HEIGHT


class Player(Entity):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.speed = ENTITY_SPEED.get(name, 6)
        self.last_shot = -1000
        self.shoot_delay = 300

    def move(self):
        keys = pygame.key.get_pressed()

        if self.name == 'Player1':
            if keys[pygame.K_UP]:
                self.rect.y -= self.speed
            if keys[pygame.K_DOWN]:
                self.rect.y += self.speed
            if keys[pygame.K_LEFT]:
                self.rect.x -= self.speed
            if keys[pygame.K_RIGHT]:
                self.rect.x += self.speed

        elif self.name == 'Player2':
            if keys[pygame.K_w]:
                self.rect.y -= self.speed
            if keys[pygame.K_s]:
                self.rect.y += self.speed
            if keys[pygame.K_a]:
                self.rect.x -= self.speed
            if keys[pygame.K_d]:
                self.rect.x += self.speed

        # não sair da tela
        self.rect.clamp_ip(pygame.Rect(0, 0, WIN_WIDTH, WIN_HEIGHT))

    def shoot(self, current_time):
        if current_time - self.last_shot > self.shoot_delay:
            self.last_shot = current_time

            from code.EntityFactory import EntityFactory

            # 🔥 define qual bala usar
            if self.name == 'Player1':
                bullet_name = 'Player1Bullet'
            else:
                bullet_name = 'Player2Bullet'

            print(f"{self.name} ATIROU")

            return EntityFactory.get_entity(
                bullet_name,
                (self.rect.right, self.rect.centery)
            )

        return None