#python3.4 or higher is required in order to use selectors
import socket
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE
from datetime import datetime

sel = DefaultSelector()
request = "GET / HTTP/1.0\r\n\r\n"

request_callback = lambda sock: sock.send(request.encode())
response_callback = lambda sock: \
        print((sock.recv(1000)).decode().split("\n")[-1], 'finish at %s' % str(datetime.now())[:-7])

def get():
    sock = socket.socket()
    sock.setblocking(False)
    try:
        sock.connect(('localhost', 3000))
    except:
        pass
    sel.register(sock, EVENT_WRITE, lambda: request_callback(sock))

get_count = 4
print("starts at %s" % str(datetime.now())[:-7])
for i in range(get_count):
    get()

while True:
    events = sel.select()
    for key, _ in events:
        callback = key.data
        event = key.events
        sel.unregister(key.fileobj)
        callback()
        if event == EVENT_WRITE:
            sel.register(key.fileobj, EVENT_READ, lambda: response_callback(key.fileobj))
        elif event == EVENT_WRITE:
            sel.register(key.fileobj, EVENT_WRITE, lambda: request_callback(key.fileobj))
