from src.code.framework.Entity import Entity
from typing import List, Optional
from src.code.framework.MainGame import MainGame

# Generic scene class to manage entities
# Scene can be understood as a current game state or level
class Scene:
    def __init__(self, name: str = "Scene"):
        self.name: str = name
        self.__entities: List[Entity] = []

    def update(self):
        for entity in self.__entities:
            entity.update()

        self.__draw_entities()

    def add_entity(self, entity: Entity):
        # check if entity with the same name already exists
        self.__entities.append(entity)

    def get_entity_by_name(self, name: str) -> Optional[Entity]:
        for entity in self.__entities:
            if entity.name == name:
                return entity
        return None

    def remove_entity(self, entity: Entity):
        if entity in self.__entities:
            self.__entities.remove(entity)
            del entity
    def __draw_entities(self):
        # Sort entities by order and draw them
        sorted_entities = sorted(self.__entities, key=lambda e: -e.order)
        MainGame().screen.fill((34, 107, 38))
        for entity in sorted_entities:
            MainGame().screen.blit(entity.image, entity.rect)