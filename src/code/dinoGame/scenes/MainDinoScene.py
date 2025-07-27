from src.code.dinoGame.entities.PlayerDino import PlayerDino
from src.code.framework.Scene import Scene
from src.code.framework.MainGame import MainGame
import pygame


class MainDinoScene(Scene):
    def __init__(self, name: str = "MainDinoScene"):
        super().__init__(name)

        # Initialize the scene with necessary entities, behaviours, and behaviors
        self.add_entity(PlayerDino(image = pygame.image.load('resources/DinoGreen/IdleAnimation/DinoIdle1.png'),
                                   name = 'Player',
                                   draw_order= 100,
                                   position= (MainGame().width / 2, MainGame().height / 2)))

