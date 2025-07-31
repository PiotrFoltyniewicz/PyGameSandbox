import pygame
from typing import Tuple

def load_image(path: str, size: Tuple[int, int]) -> pygame.Surface:
    return pygame.transform.scale(pygame.image.load(path), size)