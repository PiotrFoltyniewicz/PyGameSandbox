from src.code.dinoGame.behaviours.PlayerMovement import PlayerMovement
from src.code.dinoGame.behaviours.PlayerAttack import PlayerAttack
from src.code.dinoGame.behaviours.AnimationManager import AnimationManager
from src.code.framework.Entity import Entity
import pygame

class PlayerDino(Entity):
    def __init__(self, image: pygame.Surface, name: str = "PlayerDino", draw_order: int = 0, position = (0,0)):
        super().__init__(image, name, draw_order, position)
        self.health: int = 100  # Player health
        self.speed: float = 5.0  # Movement speed

        # Image rotation
        self.player_movement: PlayerMovement = self.add_behaviour(PlayerMovement(self))
        self.player_attack: PlayerAttack = self.add_behaviour(PlayerAttack(self))


        # Initialize animations
        self.animation_manager: AnimationManager = self.add_behaviour(AnimationManager(self))
        self.animation_manager.add_animation('idle', 'resources/DinoGreen/IdleAnimation', True)
        self.animation_manager.set_default_animation('idle')
        self.animation_manager.add_animation('move', 'resources/DinoGreen/MoveAnimation', True)

    def update(self):
        super().update()
