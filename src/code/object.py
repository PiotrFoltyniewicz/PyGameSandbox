import pygame
import abc

class Object(abc.ABC):
    def __init__(self, image, position):
        self.image = image
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = position

    @abc.abstractmethod
    def update(self):
        pass

    def draw(self, surface):
        surface.blit(self.image, self.rect)