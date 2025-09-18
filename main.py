import pygame
import sys

from player import Player
from raycasting import *
from setting import *
from map import *
from object_renderer import *
from sprite_object import *
from Gestionnaire_objet import *

class Game():
    def __init__(self):
        pygame.init()
        pygame.mouse.set_visible(False)
        self.screen = pygame.display.set_mode(Resolution)
        self.clock = pygame.time.Clock()
        self.delta_time = 1
        self.new_game()

    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.object_renderer = ObjectRenderer(self)
        self.raycasting = RayCasting(self)
        self.static_sprite = SpriteObject(self)
        self.animated_sprite = AnimatedSprite(self)
        self.object_handler = ObjectHandler(self)

    def update(self):
        self.player.update()
        self.raycasting.update()
        self.object_handler.update()
        pygame.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pygame.display.set_caption(f'{self.clock.get_fps() : .1f}')

    def draw(self):

        self.screen.fill('black')
        #self.map.draw()
        #self.player.draw()
        self.object_renderer.draw()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

if __name__ == '__main__':
    game = Game()
    game.run()