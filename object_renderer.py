import pygame
from setting import *

class ObjectRenderer:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.wall_textures = self.load_wall_textures()

    def draw(self):
        self.render_game_objects()

    def render_game_objects(self):
        list_objects = self.game.raycasting.objects_to_render
        for depth, image, pos in list_objects:
            self.screen.blit(image, pos)

    @staticmethod
    def get_texture(path, res=(Texture_size, Texture_size)):
        texture = pygame.image.load(path).convert_alpha()
        return pygame.transform.scale(texture, res)

    def load_wall_textures(self):
        return {
            1: self.get_texture('Texture/1.png'),
            2: self.get_texture('Texture/2.png'),
            3: self.get_texture('Texture/3.png'),
            4: self.get_texture('Texture/4.png'),
            5: self.get_texture('Texture/5.png'),
        }
