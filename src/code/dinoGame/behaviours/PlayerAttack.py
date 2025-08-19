from pygame.examples.go_over_there import delta_time

from src.code.framework.Behaviour import Behaviour
import pygame
from src.code.framework.MainGame import MainGame
from src.code.framework.UtilityFunctions import load_image
from src.code.dinoGame.entities.Fireball import Fireball

class PlayerAttack(Behaviour):
    def __init__(self, self_entity: 'PlayerDino'):
        super().__init__(self_entity)
        self.entity = self_entity
        self.attack_cooldown_left = 0
        self.attack_cooldown = 1

    def action(self):
        time = MainGame().clock.get_time() / 1000
        if self.attack_cooldown_left > 0:
            self.attack_cooldown_left -= time

        if pygame.key.get_pressed()[pygame.K_SPACE] and self.attack_cooldown_left <= 0:
            self.attack()

    def attack(self):
        self.attack_cooldown_left = self.attack_cooldown
        if self.entity.animation_manager.orientation == 'Right':
            x = self.entity.rect.right
        else:
            x = self.entity.rect.left
        y = self.entity.rect.centery
        new_fireball: Fireball = Fireball(image=load_image('resources/Attacks/Fireball/fireball.png', (64, 64)),
                                   name='Fireball',
                                   draw_order=150,
                                   position=(x, y))
        new_fireball.animation_manager.set_orientation(self.entity.animation_manager.orientation)
        MainGame().current_scene.add_entity(new_fireball)
