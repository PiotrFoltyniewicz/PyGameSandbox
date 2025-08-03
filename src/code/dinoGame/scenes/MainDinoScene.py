from src.code.dinoGame.entities.Goblin import Goblin
from src.code.dinoGame.entities.PlayerDino import PlayerDino
from src.code.framework.Scene import Scene
from src.code.framework.MainGame import MainGame
import pygame
from src.code.framework.UtilityFunctions import load_image


class MainDinoScene(Scene):
    def __init__(self, name: str = "MainDinoScene"):
        super().__init__(name)

        # Initialize the scene with necessary entities, behaviours, and behaviors
        self.add_entity(PlayerDino(image = load_image('resources/DinoGreen/IdleAnimation/DinoIdle1.png', (64, 64)),
                                   name = 'Player',
                                   draw_order= 100,
                                   position= (MainGame().width / 2, MainGame().height / 2)))

#        self.add_entity(Goblin(image=load_image('resources/Goblin/RunAnimation/GoblinRun1.png', (64, 64)),
#                               name='Goblin',
#                               draw_order=8,
#                               position=(MainGame().width / 2 + 100, MainGame().height / 2)))