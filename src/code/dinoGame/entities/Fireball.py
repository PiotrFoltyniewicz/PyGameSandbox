from src.code.framework.Entity import Entity
from src.code.framework.MainGame import MainGame
import pygame

class Fireball(Entity):
    def __init__(self, image: pygame.Surface,
                       name: str = "Fireball",
                       draw_order: int = 12,
                       position = (0,0)):
        super().__init__(image, name, draw_order, position)
        self.speed: float = 10.0
        self.time_to_live: float = 2.0
        self.image = image
        self.rect = self.image.get_rect()



    def update(self):
        super().update()

    def move_forward(self):
        # Move the fireball forward based on its speed

