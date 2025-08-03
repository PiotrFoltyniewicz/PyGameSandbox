from pygame import Vector2

from src.code.framework.Behaviour import Behaviour
import pygame

from src.code.framework.MainGame import MainGame


class PlayerMovement(Behaviour):
    def __init__(self, self_entity: 'PlayerDino'):
        super().__init__(self_entity)
        self.entity = self_entity

    def action(self):
        keys = pygame.key.get_pressed()
        has_moved = False
        direction = Vector2
        if keys[pygame.K_LEFT]:
            self.entity.rect.x -= self.entity.speed
            self.entity.animation_manager.set_orientation('Left')
            has_moved = True
        if keys[pygame.K_RIGHT]:
            self.entity.rect.x += self.entity.speed
            self.entity.animation_manager.set_orientation('Right')
            has_moved = True
        if keys[pygame.K_UP]:
            self.entity.rect.y -= self.entity.speed
            has_moved = True
        if keys[pygame.K_DOWN]:
            self.entity.rect.y += self.entity.speed
            has_moved = True

        # Change animation based on movement
        if has_moved:
            self.entity.animation_manager.set_animation('move')
        else:
            self.entity.animation_manager.set_animation('idle')