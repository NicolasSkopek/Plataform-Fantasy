import pygame
from obj import Obj

class Menu:
    def __init__(self, image):

        self.all_sprites = pygame.sprite.Group()

        self.bg = Obj(image, 0, 0, 1180, 620, self.all_sprites)

        self.button_start = Obj("assets/start.png", 460, 239, 485/2, 284/2, self.all_sprites)

        self.change_scene = False

    def draw(self, window):
        self.all_sprites.draw(window)

    def events(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            if self.button_start.rect.collidepoint(pygame.mouse.get_pos()):
                self.change_scene = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.change_scene = True


class Restart(Menu):
    def __init__(self, image):
        super().__init__(image)
