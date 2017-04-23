#python3.5 or higher is required in order to use async/await syntax
from types import coroutine
from selectors import DefaultSelector, EVENT_WRITE, EVENT_READ
import socket
from time import time
from datetime import datetime
from collections import deque

request_str = "GET / HTTP/1.0\r\n\r\n"

@coroutine
def request(sock):
    yield sock.send(request_str.encode())

@coroutine
def response(sock):
    print((sock.recv(1000)).decode().split("\n")[-1] + (" finish at %s" % str(datetime.now())[:-7]))
    yield

@coroutine
def connect(sock):
    try:
        sock.connect(('localhost', 3000))
    except:
        pass
    yield sock

async def get():
    sock = socket.socket()
    sock.setblocking(False)
    await connect(sock)
    await request(sock)
    await response(sock)

class Loop:
    def __init__(self):
        self.sel = DefaultSelector()
        self.queue = deque()

    def create_task(self, coro):
        sock = coro.send(None)
        self.sel.register(sock, EVENT_WRITE, coro)
        self.queue.append(coro)

    def run(self):
        while self.queue:
            events = self.sel.select()
            for key, _ in events:
                coro = key.data
                event = key.events
                file_obj = key.fileobj
                self.sel.unregister(file_obj)
                try:
                    if event == EVENT_WRITE:
                        self.sel.register(file_obj, EVENT_READ, coro)
                    elif event == EVENT_READ:
                        self.sel.register(file_obj, EVENT_WRITE, coro)
                    coro.send(None)
                except StopIteration:
                    self.queue.popleft()
                except:
                    pass
        else: return
                
if __name__ == "__main__":
    loop = Loop()
    for i in range(4):
        loop.create_task(get())
    start = time()
    print("starts at %s" % str(datetime.now())[:-7])
    loop.run()
    print("totally took %.f seconds" % (time()-start))
