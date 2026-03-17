from os import isatty
from socket import AddressFamily, SocketKind, socket
from sys import stdin

from ..utils import readlines


def client_stream(address: tuple[str, int]) -> None:
    sock = socket(AddressFamily.AF_INET, SocketKind.SOCK_STREAM)
    sock.settimeout(0.001)

    sock.connect(address)

    print(f"[*] TCP connection established with: {address}")

    if isatty(stdin.fileno()):
        while True:
            data = stdin.readline()
            sock.send(data.encode())

            try:
                for line in readlines(sock):
                    print(line)
            except TimeoutError:
                continue

    else:
        data = stdin.read()
        sock.send(data.encode())

        print("[*] Sent:")
        for line in data.splitlines():
            print(f" > {line}")

        print("[*] Received:")
        for line in readlines(sock):
            print(f" > {line}")

    sock.close()
