import pygame

class Button:

    fonts = None

    
    def __init__(self, screen, x, y, w, h, box_color, text, text_size, text_color, text_color_yes):
        if Button.fonts is None:
            Button.fonts = {
                "s": pygame.font.SysFont("malgungothic", 30, True),  # 세로: 40
                "sn": pygame.font.SysFont("malgungothic", 40, True),  # 세로: 54
                "n": pygame.font.SysFont("malgungothic", 50, True),  # 세로: 67
                "nb": pygame.font.SysFont("malgungothic", 75, True),  # 세로: 100
                "b": pygame.font.SysFont("malgungothic", 100, True),  # 세로: 134
}
        self.screen = screen
        self.box_x = x
        self.box_y = y
        self.box_w = w
        self.box_h = h
        self.box_color = box_color
        self.change_color = (255, 0, 0)
        self.color_change = False
        self.rect = pygame.Rect(x, y, w, h)

        self.text = text
        self.text_size = text_size
        self.text_color = text_color
        self.text_color_yes = text_color_yes

    def handle_event(self, event:pygame.event):
        if self.text_color_yes == "y":
            if hasattr(event, "pos") and self.rect.collidepoint(event.pos):
                self.color_change = True
                if event.type == 1025:
                    return "next"
        return None
    

    def update(self):
        if self.text_color_yes == "y":
            self.color_change = self.rect.collidepoint(pygame.mouse.get_pos())


    def draw(self):
        if self.color_change:
            pygame.draw.rect(self.screen, self.change_color, (self.box_x, self.box_y, self.box_w, self.box_h))
        else:
            pygame.draw.rect(self.screen, self.box_color, (self.box_x, self.box_y, self.box_w, self.box_h))

        font = type(self).fonts[self.text_size]
        text = font.render(self.text, True, self.text_color)

        
        text_x = self.box_x + (self.box_w - text.get_width()) / 2
        text_y = self.box_y + (self.box_h - text.get_height()) / 2

        self.screen.blit(text, (text_x, text_y))



