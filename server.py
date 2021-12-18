# -*- coding: utf-8 -*-
import socket

class Server:
    """
    Сервер, через который будет происходить взаимодействие между игроками.
    """
    def __init__(self):
        self.server = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )
        self.server.bind(('', 8910))
        self.retrieveConnection()

    def retrieveConnection(self):
        """
        Осуществляет подключение, слушает клиента.
        Returns:
            None
        """

        self.server.listen(2)
        self.cliSock, self.cliAddr = self.server.accept()
        self.cliSock.send('Вы подключены!'.encode('utf-8'))
        print(f'Игрок {self.cliSock} подключен')

    def recieveFromClient(self):
        """
        Получает от клиента информацию.
        Returns:
            Данные, полученные от клиента.
        """
        data = ''
        while True:
            inp = self.cliSock.recv(1024)
            inp = inp.decode('utf-8')
            data += inp

            if not data:
                break
            return data

class Client:
    """
    Клиент (игрок), который будет принимать и посылать информацию на сервер.
    """
    def __init__(self):
        self.client = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )
        self.client.settimeout(10)
        self.client.connect(('localhost', 8910))
        self.client.settimeout(None)

    def recieveFromServer(self):
        """
        Получает от сервера информацию.
        Returns:
            Получанная с сервера информация.
        """
        while True:
            data = self.client.recv(2048)
            data = data.decode('utf-8')
            return data

    def sendToServer(self, data):
        """
        Отправляет информацию на сервер.
        Args:
            data: отправляемая информация

        Returns:
            None
        """
        data = data.encode('utf-8')
        self.client.send(data)


