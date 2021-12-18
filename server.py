# -*- coding: utf-8 -*-
import socketio
import asyncio

class Server:
    """
    Сервер, через который будет происходить взаимодействие между игроками. Принимает ивенты от Клиентов.

    """

    def __init__(self):
        sio = socketio.AsyncServer()
        self.connected = False
        self.uid = ''


        @sio.event
        def connect(sid, environ):
            if not self.connected:
                self.connected = True
                self.uid = sid

        @sio.event
        async def get_message(sid, data):
            print("message ", data)

        @sio.event
        def disconnect(sid):
            self.connected = False
            self.uid = ''

        if __name__ == '__main__':
            web.run_app(app)




  #      sio.emit('my event', {'data': 'foobar'})

class Client:
    """
    Класс Клиента (игрока), отправляет ивенты на Сервер

    """
    def __init__(self):


        self.sio = socketio.AsyncClient()

        @self.sio.event
        async def connect(ip, port):
            print('connection established')


        @self.sio.event
        async def my_message(data):
            print('message received with ', data)
            await self.sio.emit('my response', {'response': 'my response'})

        @self.sio.event
        async def get_message(message):
            print(message['message'])

        @self.sio.event
        async def disconnect(ip, port):
            print('disconnected from server')

    def connectToServer(self, ip, port):
        self.sio.connect(f'http://{ip}:{port}')
        self.sio.wait()

