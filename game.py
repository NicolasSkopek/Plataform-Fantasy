from obj import *
import pygame

class Game:

    def __init__(self):

        self.all_sprites = pygame.sprite.Group()
        self.all_platforms = pygame.sprite.Group()
        self.all_crystals = pygame.sprite.Group()
        self.all_enemies = pygame.sprite.Group()


        self.bg = Obj("assets/test_bg.png", 0, 0, 576*2.3, 324*2.3, self.all_sprites)

        # self.campfire = Obj("assets/campfire.png", 970, 390, 463 / 4, 435 / 4, self.all_sprites)

        self.tree0 = Obj("assets/tree0.png", 40, 225, 48*5.5, 48*5.5, self.all_sprites)
        self.tree1 = Obj("assets/tree1.png", 380, 225, 48 * 5.5, 48 * 5.5, self.all_sprites)
        self.tree2 = Obj("assets/tree0.png", 440, 225, 48 * 5.5, 48 * 5.5, self.all_sprites)
        self.tree3 = Obj("assets/tree1.png", 960, 225, 48 * 5.5, 48 * 5.5, self.all_sprites)

        self.plat0 = Obj("assets/plat01.png", 25, 480, 982 / 4.5, 558 / 4.5, self.all_sprites, self.all_platforms)
        self.plat1 = Obj("assets/plat21.png", 380, 478, 1636 / 4.8, 533 / 4.8, self.all_sprites, self.all_platforms)
        self.plat2 = Obj("assets/plat11.png", 850, 475, 1438 / 4.5, 541 / 4.5, self.all_sprites, self.all_platforms)

        self.crystal0 = Obj("assets/crystal.png", 420, 320, 64, 64, self.all_sprites, self.all_crystals)
        self.crystal1 = Obj("assets/crystal.png", 650, 320, 64, 64, self.all_sprites, self.all_crystals)
        self.crystal2 = Obj("assets/crystal.png", 1100, 320, 64, 64, self.all_sprites, self.all_crystals)

        self.enemy0 = Enemy("assets/enemy0.png", 530, 405, 36*2, 38*2, self.all_sprites, self.all_enemies)
        self.enemy1 = Enemy("assets/enemy0.png", 880, 405, 36 * 2, 38 * 2, self.all_sprites, self.all_enemies)
        self.enemy2 = Enemy("assets/enemy0.png", 1100, 405, 36 * 2, 38 * 2, self.all_sprites, self.all_enemies)

        self.player = Knight("assets/knight/idle0.png", 25, 350, 41*2, 67*2, self.all_sprites)

        self.hud = Obj("assets/hud.png", 0, 0, 702 / 3, 410 / 3, self.all_sprites)

        self.life_icons = [
            Obj("assets/icon_head.png", 114, 45, 27 / 1.2, 40 / 1.2, self.all_sprites),
            Obj("assets/icon_head.png", 145, 45, 27 / 1.2, 40 / 1.2, self.all_sprites),
            Obj("assets/icon_head.png", 180, 45, 27 / 1.2, 40 / 1.2, self.all_sprites),
        ]

        self.crystal_icons = [
            Obj("assets/icon_crystal.png", 75, 80, 20 * 2.4, 20 * 2.4, self.all_sprites),
            Obj("assets/icon_crystal.png", 98, 80, 20 * 2.4, 20 * 2.4, self.all_sprites),
            Obj("assets/icon_crystal.png", 121, 80, 20 * 2.4, 20 * 2.4, self.all_sprites),
        ]
    def draw(self, window):
        self.all_sprites.draw(window)

    def update(self):
        self.all_sprites.update()
        self.player.collisions(self.all_platforms, False, "platform")
        self.player.collisions(self.all_crystals, True, "crystal")
        self.player.collisions(self.all_enemies, False, "enemy")
        self.HUD()

    def HUD(self):
        for i in range(3):
            if i < self.player.pts:
                self.crystal_icons[i].rect.x = [75, 98, 121][i]
            else:
                self.crystal_icons[i].rect.x = -200

        for i in range(3):
            if i < self.player.hp:
                self.life_icons[i].image = pygame.image.load("assets/icon_head.png")
            else:
                self.life_icons[i].image = pygame.image.load("assets/dead_head.png")
