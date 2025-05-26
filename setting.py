import math

Resolution = Largeur, Longueur = 1600, 900
FPS = 60

player_pos = 1.5, 5
player_angle = 0
player_speed = 0.05
player_rotation_speed = 0.002

FOV = math.pi /3
Moitie_FOV = FOV /2
nb_ray = Largeur//2
Moitie_nb_rays = nb_ray//2
delta_angle = FOV / nb_ray
Max_depth = 20