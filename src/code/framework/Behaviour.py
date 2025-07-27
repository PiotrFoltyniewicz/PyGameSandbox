from src.code.framework.Entity import Entity

# Bahaviour class that serves as a base for all behaviours
# They define behaviors or properties that can be added to entities
# They allow for modular design and separation of concerns
class Behaviour:
    def __init__(self, self_entity: Entity):
        self.entity = self_entity

    def action(self):
        raise NotImplementedError("This method should be overridden by subclasses")