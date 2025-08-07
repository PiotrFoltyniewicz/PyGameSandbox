import pygame.image
from src.code.framework.UtilityFunctions import *
from src.code.framework.Behaviour import Behaviour
from src.code.framework.Entity import Entity
from src.code.dinoGame.other.Animation import Animation
import pygame
import sys
import os
from typing import Dict, List

class AnimationManager(Behaviour):
    def __init__(self, self_entity: Entity):
        super().__init__(self_entity)
        self.entity = self_entity
        self.default_animation: Animation | None= None
        self.current_animation: Animation | None = None
        self.animations = {}
        self.orientation: str = 'Right'

    def add_animation(self, name: str, path_to_animation: str, loop: bool, target_size = (64, 64)):
        # load all images in the directory and add them to the animation
        frames = []
        for image_file in sorted(os.listdir(path_to_animation)):
            frames.append(load_image(os.path.join(path_to_animation, image_file), target_size))

        self.animations[name] = Animation(name, frames, loop)

    def set_default_animation(self, name: str):
        if name in self.animations:
            self.default_animation = self.animations[name]
        else:
            raise ValueError(f"Default animation '{name}' not found")

    def set_animation(self, name: str):
        if self.current_animation is not None and name == self.current_animation.name:
            return
        if name in self.animations:
            self.current_animation = self.animations[name]
            self.current_animation.reset()
        else:
            raise ValueError(f"Animation '{name}' not found")

    def set_orientation(self, new_orientation: str):
        self.orientation = new_orientation

    def action(self):
        is_running: bool = self.current_animation.update()
        if not is_running:
            if self.default_animation is not None:
                self.set_animation(self.default_animation.name)
            else:
                raise ValueError("No default animation set")

        self.entity.image = self.current_animation.get_current_frame()

        if self.orientation == 'Left':
            self.entity.image = pygame.transform.flip(self.current_animation.get_current_frame(), True, False)