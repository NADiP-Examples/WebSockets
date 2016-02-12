import sys
from pgu import gui
import pygame
import websocket

RESX = 400
RESY = 200
FPS = 40


def on_message(message):
    print(message)


def on_btn_click(value):
    print(value)
    ws.send("Hello, World")
    result = ws.recv()
    print("result = ", result)

# INIT
screen = pygame.display.set_mode((RESX, RESY))
app = gui.App()

# SOCKETS
ws = websocket.create_connection("ws://127.0.0.1:8888/websocket")
# ws.setblocking(0)
# ws = websocket.WebSocketApp("ws://127.0.0.1:8888/websocket", on_message=on_message)
# ws.on_open = ws.run_forever()

button = gui.Button('Send message')
button.connect(gui.CLICK, on_btn_click, 'OK')
app.init(widget=button)
# app.run()
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sys.exit()
        else:
            app.event(event)
    dt = clock.tick(FPS)
    screen.fill((0, 0, 0))
    app.paint()
    pygame.display.flip()
