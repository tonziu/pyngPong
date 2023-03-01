import pygame

class Menu():
    def __init__(self, screen):
        self.screen = screen
        self._init_components()
        
    def _init_components(self):
        self.surf = pygame.Surface(self.screen.get_size())
        self.font = pygame.font.SysFont('Arial0', 30)
        self.text_surf = self.font.render("Press the bar space to play", True, (255, 255, 255))

    def process_input(self, event):
        pass

    def update(self):
        pass

    def render(self):
        self.surf.fill((0, 0, 0))
        text_rect = self.text_surf.get_rect()
        text_rect.center = self.surf.get_rect().center
        self.surf.blit(self.text_surf, text_rect)
        self.screen.blit(self.surf, (0, 0))
