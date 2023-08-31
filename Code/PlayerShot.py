from Code.Entity import Entity
from Code.const import ENTITY_SPEED


class PlayerShot(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def Move(self):
        self.rect.centerx += ENTITY_SPEED[self.name]

