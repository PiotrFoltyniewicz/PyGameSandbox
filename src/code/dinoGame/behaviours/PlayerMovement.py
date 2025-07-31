from src.code.framework.Behaviour import Behaviour
import pygame

from src.code.framework.MainGame import MainGame


class PlayerMovement(Behaviour):
    def __init__(self, self_entity: 'PlayerDino'):
        super().__init__(self_entity)
        self.entity = self_entity

    def action(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.entity.rect.x -= self.entity.speed
            self.entity.set_orientation('Left')
        if keys[pygame.K_RIGHT]:
            self.entity.rect.x += self.entity.speed
            self.entity.set_orientation('Right')
        if keys[pygame.K_UP]:
            self.entity.rect.y -= self.entity.speed
        if keys[pygame.K_DOWN]:
            self.entity.rect.y += self.entity.speed