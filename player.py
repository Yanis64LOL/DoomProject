from setting import *
import pygame
import math

class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = player_pos
        self.angle = player_angle
        self.shot = False
        self.health = 100
        self.joystick = pygame.joystick.Joystick(0)
        self.joystick.init()

    def check_game_over(self):
        if self.health < 1:
            self.game.object_renderer.game_over()
            pygame.display.flip()
            pygame.time.delay(1500)
            self.game.new_game()
            self.game.run()

    def get_damage(self, damage):
        self.health -= damage
        self.game.object_renderer.player_damage()
        self.game.sound.player_pain.play()
        self.check_game_over()

    def get_health(self):
        if self.health < player_max_health:
            if player_max_health < self.health + 25:
                self.health += (player_max_health - self.health)
            else:
                self.game.player.health += 25
        self.game.object_renderer.player_heal()

    def single_fire_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.JOYBUTTONDOWN:
            if (event.button == 1 or event.button == 10) and not self.shot and not self.game.weapon.reloading:
                self.game.sound.shotgun.play()
                self.shot = True
                self.game.weapon.reloading = True

    def move(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0
        speed = player_speed
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a

        keys = pygame.key.get_pressed()
        if keys[pygame.K_z] or self.joystick.get_axis(1) < -0.5:
            dx += speed_cos
            dy += speed_sin
        if keys[pygame.K_s] or self.joystick.get_axis(1) > 0.5:
            dx += -speed_cos
            dy += -speed_sin
        if keys[pygame.K_q] or self.joystick.get_axis(0) < -0.5:
            dx += speed_sin
            dy += -speed_cos
        if keys[pygame.K_d] or self.joystick.get_axis(0) > 0.5:
            dx += -speed_sin
            dy += speed_cos

        self.check_wall_collision(dx, dy)

        if keys[pygame.K_LEFT]  or self.joystick.get_axis(2) < -0.5:
            self.angle -= player_rotation_speed * self.game.delta_time
        if keys[pygame.K_RIGHT] or self.joystick.get_axis(2) > 0.5:
            self.angle += player_rotation_speed * self.game.delta_time
        self.angle %= math.tau

    def check_wall(self, x, y):
        return (x, y) not in self.game.map.world_map

    def check_wall_collision(self, dx, dy):
        scale = player_size_scale / self.game.delta_time
        if self.check_wall(int(self.x + dx*scale), int(self.y)):
            self.x += dx
        if self.check_wall(int(self.x), int(self.y + dy*scale)):
            self.y += dy

    def draw(self):
        pygame.draw.line(self.game.screen, 'yellow', (self.x * 100, self.y * 100),
                         (self.x * 100 + Largeur * math.cos(self.angle),
                          self.y * 100 + Largeur * math.sin(self.angle)), 2)
        pygame.draw.circle(self.game.screen, 'green', (self.x * 100, self.y * 100), 15)

    def mouse_control(self):
        mx, my = pygame.mouse.get_pos()
        if mx < mouse_border_left or mx > mouse_border_right:
            pygame.mouse.set_pos([Moitié_largeur, Moitié_longueur])
        self.rel = pygame.mouse.get_rel()[0]
        self.rel = max(-mouse_max_rel, min(mouse_max_rel, self.rel))
        self.angle += self.rel * mouse_sensitivity * self.game.delta_time

    def update(self):
        self.move()
        self.mouse_control()

    @property
    def pos(self):
        return self.x, self.y

    @property
    def map_pos(self):
        return int(self.x), int(self.y)

