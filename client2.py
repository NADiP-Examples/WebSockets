import threading
import websocket
import time


def on_message(ws, message):
    print("message = ", message)


def on_open(ws):
    t2.start()


def main():
    while True:
        print('send message')
        ws.send('Hello')
        time.sleep(1)

ws = websocket.WebSocketApp("ws://127.0.1.1:8888/websocket", on_message=on_message,
                                                             on_open=on_open)
# init threads
t1 = threading.Thread(target=ws.run_forever)
t2 = threading.Thread(target=main)

t1.start()
