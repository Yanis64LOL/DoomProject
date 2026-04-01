import pygame

from sprite_object import *

class Items(SpriteObject):

    def __init__(self, game, path="Sprites/Item_heal/0.png",
                 pos=(10.5, 3.5), scale=0.3, shift=1.25):
        super().__init__(game, path, pos, scale, shift)

    def check_collision(self):
        return int(self.game.player.pos[0]) in range(int(self.x-2), int(self.x+2)) \
            and int(self.game.player.pos[1]) in range(int(self.y-2), int(self.y+2))

    def draw(self):
        pygame.draw.circle(self.game.screen, 'blue', (self.x * 100, self.y * 100), 15)

class Items_Heal(Items):
    def __init__(self, game, path="Sprites/Item_heal/0.png",
                 pos=(10.5, 3.5), scale=0.3, shift=1.25):
        super().__init__(game, path, pos, scale, shift)
        self.trigger = False


    def Add_health(self):
        if self.check_collision() and not self.trigger:
            self.game.player.get_health()
            self.image = pygame.image.load("Sprites/Item_heal/1.png").convert_alpha()
            self.trigger = True


    def update(self):
        super().update()
        self.Add_health()