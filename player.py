import pygame

class Player():
    def __init__(self, surf):
        self.surf = surf
        self.rect = pygame.Rect(0, 0, 15, 80)
        self._init_properties()

    def _init_properties(self):
        self.rect.x = self.surf.get_rect().x + self.rect.w
        self.rect.y = self.surf.get_rect().h//2 - self.rect.h//2
        self.speed = 30
        self.dy = 0

    def _move(self):
        self.rect.top += self.dy * self.speed

    def _check_bounds(self):
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= self.surf.get_rect().h:
            self.rect.bottom = self.surf.get_rect().h

    def update(self):
        self._move()
        self._check_bounds()

    def set_dir(self, dy):
        self.dy = dy

    def render(self):
        pygame.draw.rect(self.surf, (255, 255, 255), self.rect)


    
