from src.code.framework.Behaviour import Behaviour
import pygame

class PlayerAttack(Behaviour):
    def __init__(self, self_entity: 'Player'):
        super().__init__(self_entity)
        self.entity = self_entity
        self.attack_cooldown_left = 0
        self.attack_cooldown = 10

    def action(self):
        # Add cooldown management
        # HERE

        if pygame.key.get_pressed()[pygame.K_SPACE]:
            self.attack()

    def attack(self):
        # Attack behaviour
        # 1. Check orientation of the player
        # 2. Spawn fireball in the correct direction
        pass