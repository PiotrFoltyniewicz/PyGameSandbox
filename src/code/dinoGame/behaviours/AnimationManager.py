import pygame.image
from src.code.framework.UtilityFunctions import *
from src.code.framework.Behaviour import Behaviour
from src.code.framework.Entity import Entity
import pygame
import sys
import os
from typing import Dict, List

class AnimationManager(Behaviour):
    def __init__(self, self_entity: Entity):
        super().__init__(self_entity)
        self.entity = self_entity
        self.default_animation = None
        self.animations = {}

        self.current_animation = None
        self.loop = True

        # 0 - each frame is displayed for 1 frame
        # 1 - each frame is displayed for 2 frames, etc.
        self.frames_between = 6
        self.current_frame = 0

        self.current_anim_frame = 0

    def add_animation(self, name: str, path_to_animation: str):
        # load all images in the directory and add them to the animation
        frames = []
        for image_file in sorted(os.listdir(path_to_animation)):
            frames.append(load_image(os.path.join(path_to_animation, image_file), (64, 64)))

        self.animations[name] = frames

    def set_default_animation(self, name: str):
        if name in self.animations:
            self.default_animation = self.animations[name]
        else:
            raise ValueError(f"Default animation '{name}' not found")

    def set_animation(self, name: str):
        if name in self.animations:
            self.current_animation = self.animations[name]
        else:
            raise ValueError(f"Animation '{name}' not found")


    def action(self):
        if self.current_animation:
            self.current_frame += 1

            if self.current_frame == self.frames_between:
                self.entity.image = self.current_animation[self.current_anim_frame]
                self.current_anim_frame += 1
                if self.current_anim_frame >= len(self.current_animation):
                    self.current_anim_frame = 0
                self.current_frame = 0
