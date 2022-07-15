import eventlet
import socketio

sio = socketio.Server()


@sio.event
def connect(sid, environ):
    print('connect ', sid)


@sio.event
def my_message(sid, data):
    print('message ', data)


@sio.event
def disconnect(sid):
    print('disconnect ', sid)


if __name__ == '__main__':

    app = socketio.WSGIApp(sio, static_files={
        '/': {'content_type': 'text/html', 'filename': 'index.html'}
    })

    wsgi_server = eventlet.listen(('localhost', 5000))
    eventlet.wsgi.server(wsgi_server, app)
