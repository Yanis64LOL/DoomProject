import pygame

class Sound:
    def __init__(self, game):
        self.game = game
        pygame.mixer.init()
        self.path = 'Sound/'
        self.shotgun = pygame.mixer.Sound(self.path + 'shotgun.wav')