import pygame
from setting import *

class ObjectRenderer:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.wall_textures = self.load_wall_textures()
        self.sky_image = self.get_texture('Texture/sky.png', (Largeur, Moitié_longueur))
        self.sky_offset = 0

    def draw(self):
        self.draw_background()
        self.render_game_objects()

    def draw_background(self):
        self.sky_offset = (self.sky_offset + 4.5 * self.game.player.rel) % Largeur
        self.screen.blit(self.sky_image, (-self.sky_offset, 0))
        self.screen.blit(self.sky_image, (-self.sky_offset + Largeur, 0))

        pygame.draw.rect(self.screen, floor_color, (0, Moitié_longueur, Largeur, Longueur))
    def render_game_objects(self):
        list_objects = sorted(self.game.raycasting.objects_to_render, key=lambda t: t[0], reverse = True)
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
