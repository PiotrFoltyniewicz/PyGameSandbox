from src.code.framework.Entity import Entity
from src.code.framework.MainGame import MainGame
from src.code.dinoGame.behaviours.GoblinMovement import GoblinMovement
from src.code.dinoGame.behaviours.AnimationManager import AnimationManager
import pygame

class Goblin(Entity):
    def __init__(self, image: pygame.Surface,
                       name: str = "Goblin",
                       draw_order: int = 8,
                       position = (0,0)):
        super().__init__(image, name, draw_order, position)
        self.health = 100
        self.attack_power = 10
        self.speed = 2
        self.image = image

        self.goblin_movement: GoblinMovement = self.add_behaviour(GoblinMovement(self))

        # Initialize animations
        self.animation_manager: AnimationManager = self.add_behaviour(AnimationManager(self))
        self.animation_manager.add_animation('run', 'resources/Goblin/RunAnimation', True)
        self.animation_manager.add_animation('spawn', 'resources/Goblin/SpawnAnimation', False)
        self.animation_manager.set_default_animation('run')
        self.animation_manager.set_animation('spawn')



    def update(self):
        if self.animation_manager.current_animation.name == 'run':
            self.goblin_movement.set_move_target(MainGame().current_scene.get_entity_by_name('Player').rect.center)
        super().update()
