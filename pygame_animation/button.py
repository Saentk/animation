import pygame as p

class Button():
    def __init__(self, screen, x, y, w, h, text):
        self.screen = screen
        self.image = p.Surface((w, h))
        self.image.fill((0, 255, 0))
        font = p.font.Font(None, 24)
        self.text = text
        render_text = font.render(text, True, (0, 0, 0))
        text_rect = render_text.get_rect(center=self.image.get_rect().center)
        self.image.blit(render_text, text_rect)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.active = True

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def handle_event(self, event, lst):
        if event.type == p.MOUSEBUTTONDOWN and self.active:
            mouse_pos = p.mouse.get_pos()
            if self.rect.collidepoint(mouse_pos):
                self.handle_pos(lst)
                self.active = False
                p.time.set_timer(p.USEREVENT+1, 500)
        elif event.type == p.USEREVENT+1:
            self.active = True

    def create_circle(self, lst):
        for i in lst:
            if i.move_type != 'to_position' and i.move_type != 'circle':
                i.setup_circle()
                i.move_type = 'to_position'
            elif i.move_type == 'circle':
                i.move_type = 'bounce'

    def create_triangle(self, lst):
        for i in lst:
            if i.move_type != 'to_position' and i.move_type != 'triangle':
                i.setup_triangle()
                i.move_type = 'to_position'
            if i.move_type == 'triangle':
                i.move_type = 'bounce'

    def create_square(self, lst):
        for i in lst:
            if i.move_type != 'to_position' and i.move_type != 'square':
                i.setup_square()
                i.move_type = 'to_position'
            if i.move_type == 'square':
                i.move_type = 'bounce'

    def handle_pos(self, lst):
        if self.text == "Circle":
            self.create_circle(lst)
        elif self.text == "Triangle":
            self.create_triangle(lst)
        elif self.text == "Square":
            self.create_square(lst)

