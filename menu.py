import pygame
import sys

from setting import Moitié_largeur, Moitié_longueur


class Menu():
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.logo = pygame.image.load("Menu/Doom_Logo.png").convert_alpha()
        self.rect = self.logo.get_rect(center=(Moitié_largeur, Moitié_longueur - 250))
        self.button_play = Button_Play()


    def run(self):
        pygame.mouse.set_visible(True)
        while self.game.state == "menu":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                self.main_menu()
                mouse_pos = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button_play.checkforInput(mouse_pos):
                        self.game.state = "game"
                        pygame.mouse.set_visible(False)
                        self.game.new_game()
                        self.game.run()


    def main_menu(self):
        self.screen.fill("red")
        self.screen.blit(self.logo, self.rect)
        self.button_play.update(self.screen)
        pygame.display.flip()
        self.game.clock.tick(60)

class Button:
    def __init__(self, path, pos):
        self.image = pygame.image.load(path).convert_alpha()
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)

    def checkforInput(self, position):
        return position[0] in range(self.rect.left, self.rect.right)\
            and position[1] in range(self.rect.top, self.rect.bottom)

class Button_Play(Button):
    def __init__(self, path="Menu/Play Rect.png", pos=(Moitié_largeur, Moitié_longueur+75)):
        super().__init__(path, pos)
