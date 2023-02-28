import pygame
import math

from player import Player
from opponent import Opponent
from ball import Ball

class Play():
    def __init__(self, screen):
        self.screen = screen
        self._init_components()

    def _init_components(self):
        self.surf = pygame.Surface(self.screen.get_size())
        self.player = Player(self.surf)
        self.opponent = Opponent(self.surf)
        self.ball = Ball(self.surf)

    def process_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                self.player.set_dir(1)
            elif event.key == pygame.K_UP:
                self.player.set_dir(-1)
        else:
            self.player.set_dir(0)

    def _check_collisions(self):
        if self.player.rect.colliderect(self.ball.rect):
            if self.ball.rect.centery < self.player.rect.top or \
               self.ball.rect.centery > self.player.rect.bottom:
                return "player_top_bottom"
            else:
                return "player_left_right"
        if self.opponent.rect.colliderect(self.ball.rect):
            if self.ball.rect.centery < self.opponent.rect.top or \
               self.ball.rect.centery > self.opponent.rect.bottom:
                return "opponent_top_bottom"
            else:
                return "opponent_left_right"

    def _check_score(self):
        if self.ball.rect.right >= self.surf.get_rect().w:
            self.ball.reset()
        elif self.ball.rect.left <= 0:
            self.ball.reset()

    def _bounce(self, collision):
        if collision == "player_left_right":
            delta_y = self.ball.rect.centery - self.player.rect.centery
            angle = math.atan2(-delta_y, self.player.rect.h/2)
            self.ball.dx = math.cos(angle)*1.1
            self.ball.dy = math.sin(angle)*1.1
            self.ball.rect.right += 5
        elif collision == "opponent_left_right":
            delta_y = self.ball.rect.centery - self.opponent.rect.centery
            angle = math.atan2(delta_y, self.opponent.rect.h/2)
            self.ball.dx = -math.cos(angle)*1.1
            self.ball.dy = math.sin(angle)*1.1
            #self.ball.rect.right -= 5
            #self.ball.dx *= -1

    def update(self):
        self.player.update()
        self.opponent.update()
        self.ball.update()
        self.opponent.move_towards_ball(self.ball.rect)
        self._check_score()
        collision = self._check_collisions()
        self._bounce(collision) 

    def render(self):
        self.surf.fill((55, 100, 150))
        self.player.render()
        self.opponent.render()
        self.ball.render()
        self.screen.blit(self.surf, (0, 0))       
