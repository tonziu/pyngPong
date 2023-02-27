import pygame, time
from scenes import Menu, Play, End

class Pong:
    def __init__(self):
        if not pygame.get_init():
            pygame.init()
        self.window = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Pong")
        self.running = 1
        self.scenes = {'menu':Menu(pygame.display.get_surface()), 'playing':Play(pygame.display.get_surface()),
                       'ending':End(pygame.display.get_surface())} 
        self.current_state = 'menu'
        self.current_scene = self.scenes[self.current_state]
        self.clock = pygame.time.Clock()
        self.bgsound = pygame.mixer.Sound(".\Electronic Fantasy.ogg")

    def update_state(self, event):
        self.current_state = self.current_scene.check_events(event)
        self.current_scene = self.scenes[self.current_state]
        if self.current_state == 'ending':
            self.current_state = 'menu'
            self.current_scene = self.scenes[self.current_state]
        #print(self.current_state)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0
            self.update_state(event)
        return 1

    def update(self, dt):
        self.current_scene.update(dt)

    def render(self):
        self.current_scene.render()
        pygame.display.update()

    def run(self):
        prev_time = time.time()
        self.bgsound.play(-1)
        while(self.running):    
            self.clock.tick(60)
            now = time.time()
            dt = now - prev_time
            prev_time = now
            self.running = self.check_events()
            self.update(dt)
            self.render()
        pygame.quit()




