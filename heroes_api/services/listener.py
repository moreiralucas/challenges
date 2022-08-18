"""Socket.io Module"""
from typing import Optional
from flask import Flask
import socketio
from models import Threat

sio = socketio.Client()

class SocketHeroes:
    """Socket Heroes class"""

    def __init__(self) -> None:
        self.app: Optional[Flask] = None

    def start_socketio_connection(self, app: Flask):
        """Call socker io connect method to start the connection"""
        self.app = app
        sio.connect("https://zrp-challenge-socket.herokuapp.com/")

    def stop_socketio_connection(self):
        """Call socker io disconnect method to stop the connection"""
        sio.disconnect()


    def wat_socketio_connection(self):
        """Wait until the connection with the server ends"""
        sio.wait()


socket_heroes = SocketHeroes()

@sio.event
def connect():
    """Connect event"""
    print("connected to server")


@sio.event
def disconnect():
    """Disconnect event"""
    print("disconnected from server")


@sio.event
def occurrence(*args):
    """Occurrence event"""
    print("args:", args)
    with socket_heroes.app.app_context():
        threat: Threat = Threat.from_json(args[0])
        threat.save()
