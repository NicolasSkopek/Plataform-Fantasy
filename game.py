from obj import *
import pygame

class Game:

    def __init__(self):

        self.all_sprites = pygame.sprite.Group()
        self.all_platforms = pygame.sprite.Group()
        self.all_crystals = pygame.sprite.Group()
        self.all_enemies = pygame.sprite.Group()


        # self.bg = Obj("assets/bg3.jpg", 0, 0, 1180, 620, self.all_sprites)
        self.bg = Obj("assets/test_bg.png", 0, 0, 576*2.3, 324*2.3, self.all_sprites)

        self.tree0 = Obj("assets/tree0.png", 40, 225, 48*5.5, 48*5.5, self.all_sprites)
        self.tree1 = Obj("assets/tree1.png", 380, 225, 48 * 5.5, 48 * 5.5, self.all_sprites)
        self.tree2 = Obj("assets/tree0.png", 440, 225, 48 * 5.5, 48 * 5.5, self.all_sprites)
        self.tree3 = Obj("assets/tree1.png", 960, 225, 48 * 5.5, 48 * 5.5, self.all_sprites)

        self.plat0 = Obj("assets/plat01.png", 25, 480, 982 / 4.5, 558 / 4.5, self.all_sprites, self.all_platforms)
        self.plat1 = Obj("assets/plat21.png", 380, 478, 1636 / 4.5, 533 / 4.5, self.all_sprites, self.all_platforms)
        self.plat2 = Obj("assets/plat11.png", 850, 475, 1438 / 4.5, 541 / 4.5, self.all_sprites, self.all_platforms)

        self.crystal0 = Obj("assets/crystal.png", 460, 320, 64, 64, self.all_sprites, self.all_crystals)
        self.crystal1 = Obj("assets/crystal.png", 650, 320, 64, 64, self.all_sprites, self.all_crystals)
        self.crystal2 = Obj("assets/crystal.png", 1100, 320, 64, 64, self.all_sprites, self.all_crystals)

        self.enemy0 = Obj("assets/enemy0.png", 400, 400, 42*2, 39*2, self.all_sprites, self.all_enemies)
        self.enemy1 = Obj("assets/enemy0.png", 880, 400, 42 * 2, 39 * 2, self.all_sprites, self.all_enemies)
        self.enemy2 = Obj("assets/enemy0.png", 1100, 400, 42 * 2, 39 * 2, self.all_sprites, self.all_enemies)

        self.player = Knight("assets/knight/idle0.png", 25, 350, 41*2, 67*2, self.all_sprites)

        self.hud = Obj("assets/hud.png", 0, 0, 702 / 3, 410 / 3, self.all_sprites)

    def draw(self, window):
        self.all_sprites.draw(window)

    def update(self):
        self.all_sprites.update()
        self.player.collisions(self.all_platforms, False)
