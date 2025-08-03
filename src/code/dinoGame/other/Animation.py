import pygame
from typing import List
from src.code.framework.UtilityFunctions import *

class Animation:
    def __init__(self, name: str, frames: List[pygame.Surface], loop: bool = True):
        self.name = name
        self.frames = frames
        self.loop = loop
        self.current_frame_index = 0
        self.game_frames_between = 6
        self.current_game_frame = 0

    def get_current_frame(self) -> pygame.Surface:
        return self.frames[self.current_frame_index]

    def reset(self):
        self.current_frame_index = 0
        self.current_game_frame = 0

    # If animation is finished, it returns False
    def update(self) -> bool:
        self.current_game_frame += 1
        if self.current_game_frame >= self.game_frames_between:
            self.current_game_frame = 0
            self.current_frame_index += 1
            if self.current_frame_index >= len(self.frames):
                if self.loop:
                    self.current_frame_index = 0
                    return True
                else:
                    self.reset()
                    return False
        return True