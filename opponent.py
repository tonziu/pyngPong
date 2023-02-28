import pygame
import math 

class Opponent():
    def __init__(self, surf):
        self.surf = surf
        self.rect = pygame.Rect(0, 0, 15, 80)
        self._init_properties()

    def _init_properties(self):
        self.rect.x = self.surf.get_rect().w - 2*self.rect.w
        self.rect.y = self.surf.get_rect().h//2 - self.rect.h//2
        self.speed = 25
        self.dy = 0

    def _check_bounds(self):
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= self.surf.get_rect().h:
            self.rect.bottom = self.surf.get_rect().h

    def move_towards_ball(self, ball_rect):
        if ball_rect.centerx > self.rect.right:
            return
        lerp_f = 0.5
        delta_y = ball_rect.centery - self.rect.centery
        if delta_y > 10:
            direction = 1
        elif delta_y < -10:
            direction = -1
        else:
            direction = 0
        self.rect.centery += direction * self.speed * lerp_f


    def update(self):
        self._check_bounds()

    def set_dir(self, dy):
        self.dy = dy

    def render(self):
        pygame.draw.rect(self.surf, (20, 25, 30), self.rect)
