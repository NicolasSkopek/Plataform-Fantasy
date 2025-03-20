from game import Game
import pygame

class Main:
    def __init__(self):
        self.window = pygame.display.set_mode([1180, 620])
        pygame.display.set_caption("Plataform Fantasy")

        icon = pygame.image.load("assets/icon_crystal.PNG")
        pygame.display.set_icon(icon)

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
        while self.loop:
            self.draw()
            self.events()
            pygame.display.flip()
            self.fps.tick(30)

Main().update()