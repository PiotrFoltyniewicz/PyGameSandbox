from src.code.framework.Behaviour import Behaviour
from src.code.framework.Entity import Entity

from typing import Dict, List

class AnimationManager(Behaviour):
    def __init__(self, self_entity: Entity):
        super().__init__(self_entity)
        self.entity = self_entity
        self.current_animation = None
        self.animations = {}
        self.loop = False

        # 0 - each frame is displayed for 1 frame
        # 1 - each frame is displayed for 2 frames, etc.
        self.frames_between = 0

    def add_animation(self, name: str, frames: list):
        self.animations[name] = frames

    def set_animation(self, name: str):
        if name in self.animations:
            self.current_animation = self.animations[name]
        else:
            raise ValueError(f"Animation '{name}' not found")

    def update(self):
        if self.current_animation:
            # Logic to update the current animation frame
            pass  # Placeholder for actual animation logic