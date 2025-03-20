import pygame


class Obj(pygame.sprite.Sprite):
    def __init__(self, image, x, y, width = None, height = None, *groups):
        super().__init__(*groups)

        self.new_image = pygame.image.load(image)
        if width and height:
            self.new_image = pygame.transform.scale(self.new_image, (width, height))

        self.image = self.new_image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Knight(Obj):
    def __init__(self, image, x, y, width = None, height = None, *groups):
        super().__init__(image, x, y, width, height, *groups)

        self.vel = 6
        self.grav = 1

        self.walking_right = False
        self.walking_left = False
        self.jumping = False

    def update(self, *args):
        self.gravity()
        self.movement()

    def gravity(self):
        self.vel += self.grav
        self.rect.y += self.vel

        if self.vel >= 20:
            self.vel = 20

    def collisions(self, group, kill):
        col = pygame.sprite.spritecollide(self, group, kill)

        if col:
            self.rect.bottom = col[0].rect.top


    def events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                self.walking_right = True
            elif event.key == pygame.K_a:
                self.walking_left = True
            elif event.key == pygame.K_SPACE:
                self.vel *= -1
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                self.walking_right = False
            elif event.key == pygame.K_a:
                self.walking_left = False
            elif event.key == pygame.K_SPACE:
                self.vel *= -1

    def movement(self):
        if self.walking_right:
            self.rect.x += 8
        elif self.walking_left:
            self.rect.x -= 8






