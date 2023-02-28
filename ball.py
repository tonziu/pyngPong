import pygame
import random

class Ball():
    def __init__(self, surf):
        self.surf = surf
        self.rect = pygame.Rect(0, 0, 12, 12)
        self._init_properties()

    def _init_properties(self):
        self.rect.x = self.surf.get_rect().w//2 + self.rect.w//2
        self.rect.y = self.surf.get_rect().h//2 - self.rect.h//2
        self.speed = 20
        self.dx = -0.5
        self.dy = -0.5

    def _move(self):
        self.rect.x += self.dx * self.speed
        self.rect.y += self.dy * self.speed

    def _check_bounds(self):
        if self.rect.top <= 0:
            self.rect.top = 0
            self.dy *= -1
        elif self.rect.bottom >= self.surf.get_rect().h:
            self.rect.bottom = self.surf.get_rect().h
            self.dy *= -1

    def reset(self):
        self._init_properties()

    def update(self):
        self._move()
        self._check_bounds()

    def render(self):
        pygame.draw.rect(self.surf, (20, 25, 30),self.rect)
