import pygame
from setting import *

class ObjectRenderer:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.wall_textures = self.load_wall_textures()
        self.sky_image = self.get_texture('Texture/Doom/sky.png', (Largeur, Moitié_longueur))
        self.roof_image = self.get_texture('Texture/Backrooms/roof.png', (Largeur, Moitié_longueur))
        self.sky_offset = 0
        self.blood_screen = self.get_texture('Texture/Doom/blood_screen.png', Resolution)
        self.heal_screen = self.get_texture('Texture/Doom/heal_screen.png', Resolution)
        self.digit_size = 90
        self.digit_images = [self.get_texture(f'Texture/Doom/Digits/{i}.png', [self.digit_size] * 2)
                             for i in range(11)]
        self.digits = dict(zip(map(str, range(11)), self.digit_images))
        self.game_over_image = self.get_texture('Texture/Doom/game_over.png', Resolution)

    def draw(self):
        self.draw_background()
        self.render_game_objects()
        self.draw_player_health()

    def game_over(self):
        self.screen.blit(self.game_over_image, (0, 0))

    def draw_player_health(self):
        health = str(self.game.player.health)
        for i, char in enumerate(health):
            self.screen.blit(self.digits[char], (i * self.digit_size, 0))
        self.screen.blit(self.digits['10'], ((i + 1) * self.digit_size, 0))

    def player_damage(self):
        self.screen.blit(self.blood_screen, (0, 0))

    def player_heal(self):
        self.screen.blit(self.heal_screen, (0, 0))

    def draw_background(self):
        self.sky_offset = (self.sky_offset + 4.5 * self.game.player.rel) % Largeur
        if self.game.player.map_pos[0] < 7 and self.game.player.map_pos[1] > 12:
            self.screen.blit(self.roof_image, (-self.sky_offset, 0))
            pygame.draw.rect(self.screen, roof_color_backroom, (0, 0, Largeur, Longueur))
            self.screen.blit(self.roof_image, (0, Moitié_longueur))
        elif 12 < self.game.player.map_pos[0] < 27 and self.game.player.map_pos[1] > 22:
            pygame.draw.rect(self.screen, roof_color_wolfenstein, (0, 0, Largeur, Longueur))
            pygame.draw.rect(self.screen, floor_color_wolfenstein, (0, Moitié_longueur, Largeur, Longueur))
        else:
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
            1: self.get_texture('Texture/Doom/1.png'),
            2: self.get_texture('Texture/Doom/2.png'),
            3: self.get_texture('Texture/Doom/3.png'),
            4: self.get_texture('Texture/Doom/4.png'),
            5: self.get_texture('Texture/Doom/5.png'),
            6: self.get_texture('Texture/Backrooms/1.jpg'),
            7: self.get_texture('Texture/Wolfenstein/1.png'),
            8: self.get_texture('Texture/Wolfenstein/2.png'),
            9: self.get_texture('Texture/Wolfenstein/3.png'),
            10: self.get_texture('Texture/Wolfenstein/4.png'),
        }
