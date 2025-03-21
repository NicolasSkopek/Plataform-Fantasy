from game import Game
from menu import *
import pygame

pygame.mixer.init()

class Main:
    def __init__(self):
        self.window = pygame.display.set_mode([1180, 620])
        pygame.display.set_caption("Plataform Fantasy")

        icon = pygame.image.load("assets/icon_crystal.PNG")
        pygame.display.set_icon(icon)

        pygame.mixer_music.load("assets/sounds/ost.mp3")

        self.loop = True
        self.fps = pygame.time.Clock()

        self.menu = Menu("assets/menu.png")
        self.game = Game()
        self.restart = Restart("assets/restart.png")


    def draw(self):
        if not self.menu.change_scene:
            self.menu.draw(self.window)
        elif not self.game.change_scene:
            if not pygame.mixer_music.get_busy():
                pygame.mixer_music.play(-1)
                pygame.mixer.music.set_volume(0.5)
            self.game.draw(self.window)
            self.game.update()
        elif not self.restart.change_scene:
            pygame.mixer_music.stop()
            self.restart.draw(self.window)
        else:
            self.menu.change_scene = False
            self.game.change_scene = False
            self.restart.change_scene = False
            self.game.player.hp = 3
            self.game.player.pts = 0
            self.game.restart()

    def events(self):
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                self.loop = False
            if not self.menu.change_scene:
                self.menu.events(events)
            elif not self.game.change_scene:
                self.game.player.events(events)
            else:
                self.restart.events(events)

    def update(self):
        while self.loop:
            self.draw()
            self.events()
            pygame.display.flip()
            self.fps.tick(30)

Main().update()