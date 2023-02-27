import pygame, random, time

class Player():
    def __init__(self, screen):
        self.screen = screen
        self.rect = pygame.Rect(50, self.screen.get_height()/2-48, 16, 86)
        self.speed = 500
        self.color = (240, 242, 245)
        self.moving = 0

    def update(self, dt):
        self.rect.y += self.moving * self.speed * dt

    def render(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def check_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                self.moving = 1
            if event.key == pygame.K_UP:
                self.moving = -1
            if event.key == pygame.K_DOWN and pygame.key.get_mods() & pygame.KMOD_CTRL:
                self.speed = 1000
                self.color = (245, 193, 181)
                self.moving = 1
            if event.key == pygame.K_UP and pygame.key.get_mods() & pygame.KMOD_CTRL:
                self.speed = 1000
                self.color = (245, 193, 181)
                self.moving = -1

        elif event.type == pygame.KEYUP:
            self.color = (240, 242, 245)
            self.speed = 400
            self.moving = 0

class Opponent():
    def __init__(self, screen):
        self.screen = screen
        self.rect = pygame.Rect(self.screen.get_width()-66, self.screen.get_height()/2-48, 16, 86)
        self.speed = 450
        self.color = (240, 242, 245)
        self.moving = 0

    def update(self, dt):
        self.rect.y += self.moving * self.speed * dt

    def render(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def check_events(self, event):
        pass

class Ball():
    def __init__(self, screen):
        self.screen = screen
        self.rect = pygame.Rect(self.screen.get_width()/2-15, self.screen.get_height()/2-5, 10, 10)
        self.speed = 350
        self.color = (240, 242, 245)
        random.seed(time.time())
        self.dir = [random.randint(0, 1)*2-1, random.random()*2-1 ]

    def update(self, dt):
        self.check_borders()
        self.rect.x += self.dir[0] * self.speed * dt
        self.rect.y += self.dir[1] * self.speed * dt
        

    def render(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def check_events(self, event):
        pass

    def check_borders(self):
        if self.rect.y < 0:
            self.dir[1] *= -1.01
        elif self.rect.y > self.screen.get_height()-self.rect.h:
            self.dir[1] *= -1.01
