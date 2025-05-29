import math

Resolution = Largeur, Longueur = 1600, 900
Moitié_largeur = Largeur //2
Moitié_longueur = Longueur //2

FPS = 60

player_pos = 1.5, 5
player_angle = 0
player_speed = 0.05
player_rotation_speed = 0.002
player_size_scale = 60

mouse_sensitivity = 0.0003
mouse_max_rel = 40
mouse_border_left = 100
mouse_border_right = Largeur - mouse_border_left

floor_color = (30, 30, 30)

FOV = math.pi /3
Moitie_FOV = FOV /2
nb_ray = Largeur//2
Moitie_nb_rays = nb_ray//2
delta_angle = FOV / nb_ray
Max_depth = 20

screen_dist = Moitié_largeur /math.tan(Moitie_FOV)
scale = Largeur // nb_ray

Texture_size = 256
Moitie_texture_size = Texture_size//2