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
        self.players = []
        self.server.listen(2)
        self.cliSock, self.cliAddr = self.server.accept()
        print(f'Игрок {self.cliSock} подключен')
        self.players.append(self.cliSock)

    def recieve(self):
        """
        Получает от клиента информацию.
        Returns:
            Данные, полученные от клиента.
        """
        data = ''

        inp = self.cliSock.recv(1024)
        inp = inp.decode('utf-8')
        data += inp

        return data

    def send(self, data):
        """
        Отправляет информацию клиентам.
        Args:
            data: отправляемые данные

        Returns:
            None
        """
        for player in self.players:
            data = data.encode('utf-8')
            player.send(data)

class Client:
    """
    Клиент (игрок), который будет принимать и посылать информацию на сервер.
    """
    def __init__(self, ip, port):
        self.client = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )
        self.client.settimeout(10)
        self.client.connect((ip, port))
        self.client.settimeout(None)

    def recieve(self):
        """
        Получает от сервера информацию.
        Returns:
            Получанная с сервера информация.
        """

        data = self.client.recv(2048)
        data = data.decode('utf-8')
        return data

    def send(self, data):
        """
        Отправляет информацию на сервер.
        Args:
            data: отправляемая информация

        Returns:
            None
        """
        data = data.encode('utf-8')
        self.client.send(data)


