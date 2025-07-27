import pygame
import sys
from src.code.framework.SingletonMeta import  SingletonMeta

class MainGame(metaclass=SingletonMeta):
    def __init__(self, title='The Game', width=1280, height=640):
        self.current_scene = None

        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()

        pygame.display.set_caption('The Game')

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.current_scene.update()
            pygame.display.update()
            self.clock.tick(60)
