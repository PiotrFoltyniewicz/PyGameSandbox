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
        self.attack_cooldown = 10

    def action(self):
        # Add cooldown management
        # jeżeli attack_cooldown_left < 0 można attakować
        # inaczej nie
        # dodatkowe punkty jeżeli cooldown będzie w sekundach

        if pygame.key.get_pressed()[pygame.K_SPACE]:
            self.attack()

    def attack(self):
        # Attack behaviour
        # 1. Check orientation of the player
        # 2. Spawn fireball in the correct direction
        x = self.entity.rect.right
        y = self.entity.rect.centery
        MainGame().current_scene.add_entity(Fireball(image=load_image('resources/Attacks/fireball.png', (64, 64)),
                                   name='Fireball',
                                   draw_order=150,
                                   position=(x, y)))