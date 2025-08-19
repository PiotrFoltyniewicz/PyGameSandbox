from src.code.dinoGame.entities.Goblin import Goblin
from src.code.dinoGame.entities.PlayerDino import PlayerDino
from src.code.framework.Scene import Scene
from src.code.framework.MainGame import MainGame
import pygame
from src.code.framework.UtilityFunctions import load_image
import random

class MainDinoScene(Scene):
    def __init__(self, name: str = "MainDinoScene"):
        super().__init__(name)
        self.spawn_cooldown_left = 0
        self.spawn_cooldown = 1

        # Initialize the scene with necessary entities, behaviours, and behaviors
        self.add_entity(PlayerDino(image = load_image('resources/DinoGreen/IdleAnimation/DinoIdle1.png', (96, 96)),
                                   name = 'Player',
                                   draw_order= 100,
                                   position= (MainGame().width / 2, MainGame().height / 2)))

#        self.add_entity(Goblin(image=load_image('resources/Goblin/RunAnimation/GoblinRun1.png', (64, 64)),
#                               name='Goblin',
#                               draw_order=8,
#                               position=(MainGame().width / 2 + 100, MainGame().height / 2)))

    def update(self):
        # spawn cooldown like with the fireball
        time = MainGame().clock.get_time() / 1000
        if self.spawn_cooldown_left > 0:
            self.spawn_cooldown_left -= time

        if self.spawn_cooldown_left <= 0:
            self.spawn_goblin()
            self.spawn_cooldown_left = self.spawn_cooldown
        super().update()

    # Spawn a goblin at a random position, which is not too near the player
    def spawn_goblin(self, distance_from_player: int = 200):

        x = random.randint(0, MainGame().width)
        y = random.randint(0, MainGame().height)
        self.add_entity(Goblin(image=load_image('resources/Goblin/SpawnAnimation/GoblinSpawn1.png', (64, 64)),
                                   name='Goblin',
                                   draw_order=90,
                                   position=(x,y)))
        # 1. pick random location on the screen which is not too near the player
        # 2. spawn goblin there
        pass