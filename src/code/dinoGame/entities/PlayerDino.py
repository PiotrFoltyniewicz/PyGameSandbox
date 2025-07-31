from src.code.dinoGame.behaviours.PlayerMovement import PlayerMovement
from src.code.dinoGame.behaviours.AnimationManager import AnimationManager
from src.code.framework.Entity import Entity
import pygame

class PlayerDino(Entity):
    def __init__(self, image: pygame.Surface, name: str = "PlayerDino", draw_order: int = 0, position = (0,0)):
        super().__init__(image, name, draw_order, position)
        self.health: int = 100  # Player health
        self.speed: float = 5.0  # Movement speed

        # Image rotation
        self.orientation = 'Right'
        self.player_movement: PlayerMovement = self.add_behaviour(PlayerMovement(self))
        self.animation_manager: AnimationManager = self.add_behaviour(AnimationManager(self))

        self.animation_manager.add_animation('move', 'resources/DinoGreen/MoveAnimation')
        self.animation_manager.set_animation('move')


    # Currently only flipping Right and Left
    def set_orientation(self, new_orientation: str):
        if self.orientation != new_orientation:
            self.image = pygame.transform.flip(self.image, True, False)
            self.orientation = new_orientation

    def update(self):
        super().update()
