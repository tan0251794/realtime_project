import socketio
from aiohttp import web

sio = socketio.AsyncServer()


class SocketServer:

    def __init__(self):
        self.app = web.Application()
        self.sio = sio.attach(self.app)

    @sio.event
    def connect(self, sid, environ):
        print("connect ", sid)

    @sio.event
    async def my_message(self, sid, data):
        print(data)

    @sio.event
    def disconnect(self, sid):
        print('disconnect ', sid)


if __name__ == '__main__':
    sos = SocketServer()
    web.run_app(app=sos.app, host='localhost', port=6600)
