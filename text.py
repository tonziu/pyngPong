import pygame 

class Text:
        def __init__(self, font, canvas, color, bgcolor):
            self.font = font
            self.canvas = canvas
            self.color = color
            self.bgcolor = bgcolor
            
        def render(self, textstring, x, y, font = None):
            self.canvas.fill(self.bgcolor)
            if font:
                self.font = font
            #x = x - len(textstring)*self.font.get_height()/2
            self.surface = self.font.render(textstring, 1, self.color)
            surface_rect = self.surface.get_rect()
            x -= surface_rect.w/2
            #y -= surface_rect.w/2
            self.canvas.blit(self.surface, (x, y))

        def render_static(self, textstring, x, y, font = None):
            if font:
                self.font = font
            #x = x - len(textstring)*self.font.get_height()/2
            self.surface = self.font.render(textstring, 1, self.color)
            surface_rect = self.surface.get_rect()
            x -= surface_rect.w/2
            #y -= surface_rect.w/2
            self.canvas.blit(self.surface, (x, y))