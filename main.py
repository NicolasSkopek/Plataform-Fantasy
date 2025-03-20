from game import Game
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

        self.game = Game()


    def draw(self):
        self.game.draw(self.window)
        self.game.update()

    def events(self):
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                self.loop = False
            self.game.player.events(events)

    def update(self):
        pygame.mixer_music.play(-1)
        pygame.mixer.music.set_volume(0.5)
        while self.loop:
            self.draw()
            self.events()
            pygame.display.flip()
            self.fps.tick(30)

Main().update()