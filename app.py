import pygame

from menu import Menu
from play import Play
from quit import Quit

from enum import Enum

class GAMESCENE(Enum):
    MENU = 0
    PLAY = 1
    QUIT = 2

class App():
    def __init__(self):
        pygame.init()
        self._init_window(800, 600)
        self._init_scenes()
        self._init_variables()    
    
    def _init_window(self, w, h):
        self.screen = pygame.display.set_mode((w, h))
        pygame.display.set_caption("Pyng Pong")

    def _init_scenes(self):
        self.menu = Menu(self.screen)
        self.play = Play(self.screen)
        self.quit = Quit(self.screen)

    def _init_variables(self):
        self.running = True
        self.scene = self.menu

    def _change_scene(self, scene):
        if scene == GAMESCENE.MENU:
            self.scene = self.menu
        elif scene == GAMESCENE.PLAY:
            self.scene = self.play
        elif scene == GAMESCENE.QUIT:
            self.scene = self.quit

    def _process_input(self):
        for event in pygame.event.get():
            self.scene.process_input(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and self.scene != self.play:
                    self._change_scene(GAMESCENE.PLAY)
                elif event.key == pygame.K_q:
                    self._change_scene(GAMESCENE.QUIT)
            elif event.type == pygame.QUIT:
                self.running = False
                return 
            
    def _update(self):
        self.scene.update()

    def _render(self):
        self.scene.render()
        pygame.display.update()

    def run(self):
        clock = pygame.time.Clock()
        while self.running:
            clock.tick(30)
            self._process_input()
            self._update()
            self._render()
        pygame.quit()
