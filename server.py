import socketio

class Server:
    def __init__(self):

        sio = socketio.AsyncServer()
        app = socketio.ASGIApp(sio)

        @sio.event
        async def connect(sid, environ):
            print(sid, 'connected')

        @sio.event
        async def disconnect(sid):
            print(sid, 'disconnected')


class Client:
    def __init__(self):

        sio = socketio.AsyncClient()

        @sio.event
        async def message(data):
            print('recieved')

        @sio.on('*')
        async def catch_all(event, sid, data):
            pass
