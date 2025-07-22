import pygame
import sys
import random

# Initialization
pygame.init()
width, height = 1280, 640
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Test Game")
tile_surface = pygame.image.load('../resources/greenTile.png')
pygame.display.set_icon(tile_surface)
clock = pygame.time.Clock()

# surroundings
sky_surface = pygame.image.load('../resources/sky.png')
tile_surface = pygame.image.load('../resources/greenTile.png')
tile_surface = pygame.transform.scale(tile_surface, (64, 64))

# player
player_surface = pygame.image.load('../resources/player.png')
player_surface = pygame.transform.scale(player_surface, (64, 64))
player_rect = player_surface.get_rect(midbottom=(width // 2, height - 64))

# other objects
present_list = []
placement_array = [0] * (width // 64)

bullet_list = []

while sum(placement_array) < 3:
    random_index = random.randint(0, len(placement_array) - 1)
    placement_array[random_index] = 1

for index, val in enumerate(placement_array):
    if val == 1:
        present_surface = pygame.transform.scale(pygame.image.load("../resources/present.png"), (64, 64))
        present_rect = present_surface.get_rect(topleft=(index * 64, height - 128))
        present_list.append((present_surface, present_rect))

# Methods

def draw_surroundings():
    screen.blit(sky_surface, (0, 0))
    for i in range(width // 64):
        screen.blit(tile_surface, (i * 64, height - 64))

def draw_presents():
    for present in present_list:
        screen.blit(present[0], present[1])

def handle_bullets():
    for bullet in bullet_list:
        screen.blit(bullet[0], bullet[1])
        bullet[1].y -= 10
        if bullet[1].bottom < 0:
            bullet_list.remove(bullet)

def handle_player_present_collision():
    for present in present_list:
        if player_rect.colliderect(present[1]):
            present_list.remove(present)
            print("Present collected!")
            break


class Entity(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = image
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = position
        self.__speed = 5

    def update(self):
        screen.blit(self.image, self.rect)

class Player(Entity):
    def __init__(self):
        super().__init__(player_surface, player_rect)

    def update(self):
        super().update()
        self.__handle_movement()
        self.__handle_shoot()

    def __handle_movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
            if self.rect.right < 0:
                self.rect.left = width
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
            if self.rect.left > width:
                self.rect.right = 0

    def __handle_shoot(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            bullet_surface = pygame.Surface((5, 20))
            bullet_surface.fill('Yellow')
            bullet_rect = bullet_surface.get_rect(midbottom=(self.rect.centerx, self.rect.top))
            entities.append(Bullet(bullet_rect))

class Bullet(Entity):
    def __init__(self, position):
        surface = pygame.Surface((5, 20))
        super().__init__(surface, position)
        self.image.fill('Yellow')

    def update(self):
        super().update()
        self.rect.y -= 10

    def hit(self):
        return

entities = [Player()]

# Main game loop
while True:
    # Handle game exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    draw_surroundings()
    handle_player_present_collision()
    draw_presents()
    for entity in entities:
        entity.update()


        # Update the display
    pygame.display.update()
    clock.tick(60) # Limit to 60 FPS