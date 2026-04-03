from sprite_object import *
from npc import *
from Items import *

class ObjectHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.npc_list = []
        self.items_list = []
        self.npc_sprite_path_doom = 'Sprites/Doom/Npc/'
        self.static_sprite_path_doom = 'Sprites/Doom/Static_sprites/'
        self.anim_sprite_path_doom = 'Sprites/Doom/animated_sprites/'
        self.npc_sprite_path_wolfenstein = 'Sprites/Wolfenstein/Npc/'
        self.static_sprite_path_wolfenstein = 'Sprites/Wolfenstein/Static_sprites/'
        self.anim_sprite_path_wolfenstein = 'Sprites/Wolfenstein/animated_sprites/'
        add_sprite = self.add_sprite
        add_npc = self.add_npc
        add_items = self.add_items
        self.npc_position = {}


        #add_items(Items_Heal(game))
        #add_sprite(SpriteObject(game, path=self.static_sprite_path_wolfenstein + 'Tonneau.png', pos=(10, 5)))
        #add_sprite(AnimatedSprite(game))
        #add_sprite(AnimatedSprite(game, pos=(1.5, 1.5)))
        #add_sprite(AnimatedSprite(game, pos=(1.5, 7.5)))
        #add_sprite(AnimatedSprite(game, pos=(5.5, 3.25)))
        #add_sprite(AnimatedSprite(game, pos=(5.5, 4.75)))
        #add_sprite(AnimatedSprite(game, pos=(7.5, 2.5)))
        #add_sprite(AnimatedSprite(game, pos=(7.5, 5.5)))
        #add_sprite(AnimatedSprite(game, pos=(14.5, 1.5)))
        #add_sprite(AnimatedSprite(game, pos=(14.5, 4.5)))
        #add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(14.5, 7.5)))
        #add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(12.5, 7.5)))
        #add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(9.5, 7.5)))

        #add_npc(SoldierNPC(game))
        #add_npc(Boss(game, pos=(11.5, 4.5)))

    def update(self):
        self.npc_position = {npc.map_pos for npc in self.npc_list if npc.alive}
        [sprite.update() for sprite in self.sprite_list]
        [npc.update() for npc in self.npc_list]
        [item.update() for item in self.items_list]

    def add_npc(self, npc):
        self.npc_list.append(npc)

    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)

    def add_items(self, items):
        self.items_list.append(items)