import socketio
import asyncio

class Server: #Сервер, через который будет происходить взаимодействие между игроками
    def __init__(self):

        sio = socketio.AsyncServer()
        app = socketio.ASGIApp(sio)

        @sio.event
        async def connect(sid, environ):
            print(sid, 'connected')

        @sio.event
        async def disconnect(sid):
            print(sid, 'disconnected')

        sio.emit('my event', {'data': 'foobar'})

class Client: #Клиент (Игрок)
    def __init__(self):

        sio = socketio.AsyncClient()

        @sio.event
        async def message(data):
            print('recieved')

        @sio.on('*')
        async def catch_all(event, sid, data):
            pass

        async def main():
            await sio.connect('http://localhost:5000')
            await sio.wait()

        sio.emit('my message', {'foo': 'bar'})


