import pygame
from typing import List, TYPE_CHECKING

# Entity class that represents a game object with behaviours
# Entity can be understood as a game object, like a player, enemy, or item
# it can have multiple behaviours that define its behavior
# most likely it will have a sprite image and a rectangle for positioning
class Entity(pygame.sprite.Sprite):
    def __init__(self, image: pygame.Surface, name, draw_order, position = (0, 0)):
        super().__init__()
        self.image = pygame.transform.scale(image, (64, 64))
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.name: str = name
        # higher order means it will be drawn on top
        self.order: int = draw_order

        self.__behaviours: List['Behaviour'] = []

    def update(self):
        for behaviour in self.__behaviours:
            behaviour.action()

    def add_behaviour(self, behaviour: 'Behaviour') -> 'Behaviour':
        for existing_behaviour in self.__behaviours:
            if isinstance(existing_behaviour, type(behaviour)):
                raise ValueError(f"behaviour of type {type(behaviour).__name__} already exists.")
        self.__behaviours.append(behaviour)
        return behaviour

    def remove_behaviour(self, behaviour: 'Behaviour'):
        if behaviour in self.__behaviours:
            self.__behaviours.remove(behaviour)

    def remove_behaviour_by_type(self, behaviour_type: type):
        self.__behaviours = [c for c in self.__behaviours if not isinstance(c, behaviour_type)]