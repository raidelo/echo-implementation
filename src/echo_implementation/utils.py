from socket import socket
from typing import Generator

from .constants import CHUNK


def readlines(connection: socket) -> Generator[bytes, None, None]:
    while True:
        data = connection.recv(CHUNK)
        if len(data) == 0:
            return
        yield data
