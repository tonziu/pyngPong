import pygame, math
from text import Text
from entities import Player, Ball, Opponent

class Menu():
    def __init__(self, screen):
        self.screen = screen
        self.surface = pygame.Surface(self.screen.get_size())
        self.surface.fill((47, 51, 64))
        self.text_writer = Text(pygame.font.Font(".\ARCADE_N.ttf", 40), self.surface, (255, 255, 255), (47, 51, 64))
        self.text_writer.render_static("Pong", self.screen.get_width()/2, 50)
        self.text_writer.render_static("Press the space bar to play", self.screen.get_width()/2, 300, font = pygame.font.Font(".\ARCADE_N.ttf", 18))
              
    def update(self, dt):
        pass

    def render(self):
        self.screen.blit(self.surface, (0, 0))
        
    def check_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                return 'playing'
        return 'menu'

class Play():
    def __init__(self, screen):
        self.screen = screen
        self.surface = pygame.Surface(self.screen.get_size())
        self.surface.fill((22, 24, 28))
        self.text_writer = Text(pygame.font.Font(".\ARCADE_N.ttf", 18), self.surface, (255, 255, 255), (22, 24, 28))
        self.player_score = 0
        self.opponent_score = 0
        self.player = Player(self.screen)
        self.ball = Ball(self.screen)
        self.opponent = Opponent(self.screen) 
        self.bounce_sound = pygame.mixer.Sound(".\\bounce.mp3")

    def draw_net(self):
        for i in range(75, 550, 25):
            self.text_writer.render_static("|", self.screen.get_width()/2, i)
    
    def check_collision(self):
        #if (self.ball.rect.x <= self.player.rect.x+self.player.rect.w/2 and self.ball.rect.x > self.player.rect.x):
        if (self.ball.rect.colliderect(self.player.rect)):
            #if (self.ball.rect.y >= self.player.rect.y and self.ball.rect.y <= self.player.rect.y + self.player.rect.h):
            self.ball.dir[0] *= -1.55 
            self.ball.dir[1] = (self.player.rect.y - self.ball.rect.y)/50 + self.player.speed/200
            self.player.color = (147, 237, 168)
            self.bounce_sound.play(0)

        #if (self.ball.rect.x >= self.opponent.rect.x and self.ball.rect.x <= self.opponent.rect.x+self.opponent.rect.w//2):
        if (self.ball.rect.colliderect(self.opponent.rect)):
            
        #       if (self.ball.rect.y >= self.opponent.rect.y and self.ball.rect.y <= self.opponent.rect.y + self.opponent.rect.h):
            self.ball.dir[0] *= -1.05 
            self.ball.dir[1] = (self.opponent.rect.y - self.ball.rect.y)/50 + self.opponent.speed/200
            self.opponent.moving = 0
            self.bounce_sound.play(0)

    def check_border(self):
        if self.ball.rect.x > self.screen.get_width():
            self.ball = Ball(self.screen)
            self.player_score += 1
        elif self.ball.rect.x < 0:
            self.ball = Ball(self.screen)
            self.opponent_score += 1

    def move_opponent(self):
        self.opponent.moving = 0
        if (math.fabs(self.opponent.rect.x - self.ball.rect.x) < 300):
            if (self.opponent.rect.y > self.ball.rect.y):
                self.opponent.moving = -1
            elif (self.opponent.rect.y < self.ball.rect.y):
                self.opponent.moving = 1

    def check_scores(self):
        if (self.player_score > 6):
            return 1
        if (self.opponent_score > 6):
            return 1
        return 0

    def update(self, dt):
        self.check_collision()
        self.check_border()
        self.ball.update(dt)
        self.player.update(dt)                
        self.move_opponent()
        self.opponent.update(dt)
       
    def render(self):
        self.screen.blit(self.surface, (0, 0))
        self.text_writer.render(str(self.player_score) + "  |  " + str(self.opponent_score), self.screen.get_width()/2, 25)
        self.draw_net()
        self.ball.render()
        self.player.render()
        self.opponent.render()
        
    def check_events(self, event):
        self.player.check_events(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                self.ball = Ball(self.screen)
                self.player_score = 0
                self.opponent_score = 0
        if self.check_scores():
            return 'ending'
        return 'playing'

class End():
    def __init__(self, screen):
        self.screen = screen
        self.surface = pygame.Surface(self.screen.get_size())
        self.surface.fill((22, 24, 28))
        self.text_writer = Text(pygame.font.Font(".\ARCADE_N.ttf", 18), self.surface, (255, 255, 255), (22, 24, 28))

    def update(self, dt):
        pass
    
    def render(self):
        self.screen.blit(self.surface, (0, 0))
         
    def check_events(self, event):
        return 'ending'
