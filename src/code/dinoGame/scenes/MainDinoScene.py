import math

from src.code.dinoGame.entities.Goblin import Goblin
from src.code.dinoGame.entities.PlayerDino import PlayerDino
from src.code.framework.Scene import Scene
from src.code.framework.MainGame import MainGame
import pygame
from src.code.framework.UtilityFunctions import load_image
import random
from pygame.math import Vector2

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

        while True:
            x = random.randint(0, MainGame().width)
            y = random.randint(0, MainGame().height)
            PlayerPos: Vector2 = Vector2(self.get_entity_by_name('Player').rect.center)

            if math.sqrt((PlayerPos.x - x)**2 + (PlayerPos.y - y)**2) > distance_from_player:
                self.add_entity(Goblin(image=load_image('resources/Goblin/SpawnAnimation/GoblinSpawn1.png', (64, 64)),
                                       name='Goblin',
                                       draw_order=90,
                                       position=(x,y)))
                break