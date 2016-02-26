import sys
from pgu import gui
import pygame
import websocket

RESX = 400
RESY = 400
FPS = 40


class GuiWindow:
    def __init__(self):
        self.app = app = gui.App()
        button_send = gui.Button('Send')
        button_OK = gui.Button('OK')
        # button_send.connect(gui.CLICK, on_btn_click, 'send')
        self.rect = pygame.Rect((120, 50, 200, 50))
        table = gui.Table()
        table.tr()
        table.td(gui.Label("Button: "))
        table.td(button_send)
        table.tr()
        table.td(gui.Label("Button: "))
        table.td(button_OK)
        app.init(widget=table, screen=screen, area=self.rect)

    def event(self, event):
        self.app.event(event)

    def paint(self):
        pygame.draw.rect(screen, (0, 200, 0), self.rect, 2)
        self.app.paint()

# INIT
screen = pygame.display.set_mode((RESX, RESY))
window = GuiWindow()

# SOCKETS

clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE or event.type == pygame.QUIT:
            sys.exit()
        window.event(event)
    dt = clock.tick(FPS)
    screen.fill((0, 100, 0))
    # screen.blit(place, place.get_rect())
    window.paint()
    pygame.display.flip()
