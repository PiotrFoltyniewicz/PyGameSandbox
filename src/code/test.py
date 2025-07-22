import pygame
import sys

class Scene():
    def __init__(self):
        self.entities = []

    def run(self):
        for entity in self.entities:
            entity.update()

class MainGame(Scene):
    def run(self):
        super().run()
        pygame.display.set_caption("Main Game")
        print("Running Main Game Scene")

class Menu(Scene):

    def run(self):
        super().run()
        pygame.display.set_caption("Menu")
        print("Menu")

pygame.init()
width, height = 1280, 640
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Test Game")
clock = pygame.time.Clock()

currentScene: Scene = MainGame()

while True:
    # Handle game exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    currentScene.run()

    if isinstance(currentScene, MainGame):
        pygame.time.delay(3000)
        currentScene = Menu()



    # Update the display
    pygame.display.update()
    clock.tick(60) # Limit to 60 FPS