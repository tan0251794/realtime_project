import json
import selectors
import socket


def write(sock):
    print('Able to Write')
    sock.send(b'Hello')


def start_connections(host, port, num_conns):
    server_addr = (host, port)
    for i in range(0, num_conns):
        connid = i + 1
        print(f"Starting connection {connid} to {server_addr}")
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setblocking(False)
        sock.connect_ex(server_addr)
        events = selectors.EVENT_READ | selectors.EVENT_WRITE

        data = {
            "connid": connid,
            "msg_total": sum(len(m) for m in messages),
            "recv_total": 0,
            "messages": messages.copy(),
            "outb": ""
        }

        data = json.dumps(data).encode('utf-8')

        sel.register(sock, events, data=sock.send(data))


if __name__ == '__main__':
    sel = selectors.DefaultSelector()
    messages = ["Message 1 from client.", "Message 2 from client."]

    start_connections('localhost', 44445, 1)
