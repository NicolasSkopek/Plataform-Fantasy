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

        self.hit_sound = pygame.mixer.Sound("assets/sounds/hit.mp3")
        self.kill_sound = pygame.mixer.Sound("assets/sounds/kill.mp3")
        self.point_sound = pygame.mixer.Sound("assets/sounds/point.mp3")


        self.vel = 6
        self.grav = 1

        self.ticks = 0
        self.img = 0

        self.pts = 0
        self.hp = 3

        self.walking_right = False
        self.walking_left = False
        self.jumping = False

    def update(self, *args):
        self.gravity()
        self.movement()

    def gravity(self):
        self.vel += self.grav
        self.rect.y += self.vel

        if self.vel >= 10:
            self.vel = 10

    def collisions(self, group, kill, name):
        col = pygame.sprite.spritecollide(self, group, kill)

        if col and name == "platform":
            self.rect.bottom = col[0].rect.top
        if col and name == "crystal":
            self.point_sound.play()
            self.pts += 1
        if col and name == "enemy":
            if self.rect.y + 90 < col[0].rect.top:
                self.kill_sound.play()
                self.vel *= -1
                col[0].kill()

    def events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                self.walking_right = True
            elif event.key == pygame.K_a:
                self.walking_left = True
            elif event.key == pygame.K_SPACE:
                self.jumping = True
                self.vel *= -1.4
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                self.walking_right = False
            elif event.key == pygame.K_a:
                self.walking_left = False
            elif event.key == pygame.K_SPACE:
                self.jumping = False
                self.vel *= -1

    def movement(self):
        if self.jumping:
            if self.walking_right:
                self.anim(5, 5, "jump")
                self.image = pygame.transform.flip(self.image, False, False)
            if self.walking_left:
                self.anim(5, 5, "jump")
                self.image = pygame.transform.flip(self.image, True, False)
        if self.walking_right:
            self.rect.x += 8
            if not self.jumping:
                self.anim(5, 6, "walk")
                self.image = pygame.transform.flip(self.image, False, False)
        elif self.walking_left:
            self.rect.x -= 8
            if not self.jumping:
                self.anim(5, 6, "walk")
                self.image = pygame.transform.flip(self.image, True, False)
        else:
            self.anim(6, 3, "idle")


    def anim(self, speed, frames, name):
        self.ticks += 1
        if self.ticks >= speed:
            self.ticks = 0
            self.img += 1
        if self.img > frames:
            self.img = 0

        self.image = pygame.image.load("assets/knight/" + name + str(self.img) + ".PNG")
        if name != "jump":
            self.image = pygame.transform.scale(self.image, (41*2, 67*2))
        else:
            self.image = pygame.transform.scale(self.image, (72 * 2, 67 * 2))





