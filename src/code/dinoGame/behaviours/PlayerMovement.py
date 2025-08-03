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
        direction = Vector2(0, 0)
        if keys[pygame.K_LEFT]:
            direction.x -= self.entity.speed
            self.entity.animation_manager.set_orientation('Left')
            has_moved = True
        if keys[pygame.K_RIGHT]:
            direction.x += self.entity.speed
            self.entity.animation_manager.set_orientation('Right')
            has_moved = True
        if keys[pygame.K_UP]:
            direction.y -= self.entity.speed
            has_moved = True
        if keys[pygame.K_DOWN]:
            direction.y += self.entity.speed
            has_moved = True

        if direction.length() > 0:
            direction = direction.normalize() * self.entity.speed
            self.entity.rect.x += direction.x
            self.entity.rect.y += direction.y

        # Change animation based on movement
        if has_moved:
            self.entity.animation_manager.set_animation('move')
        else:
            self.entity.animation_manager.set_animation('idle')