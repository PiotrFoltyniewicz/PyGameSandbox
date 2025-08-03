from src.code.framework.Behaviour import Behaviour
from pygame.math import Vector2

class GoblinMovement(Behaviour):
    def __init__(self, self_entity: 'Goblin'):
        super().__init__(self_entity)
        self.entity = self_entity
        self.move_target: Vector2 | None = None

    def set_move_target(self, target: Vector2):
        self.move_target = target

    def action(self):
        # Goblins move to the target
        if self.move_target:
            direction = Vector2(self.move_target) - self.entity.rect.center
            if direction.length() > 0:
                direction = direction.normalize() * self.entity.speed
                self.entity.rect.x += direction.x
                self.entity.rect.y += direction.y

                # Flip goblin orientation based on direction
                if direction.x < 0:
                    self.entity.animation_manager.set_orientation('Left')
                else:
                    self.entity.animation_manager.set_orientation('Right')