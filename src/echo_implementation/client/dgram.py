from os import isatty
from socket import AddressFamily, SocketKind, socket
from sys import stdin

from ..constants import CHUNK


def client_dgram(address: tuple[str, int]) -> None:
    sock = socket(AddressFamily.AF_INET, SocketKind.SOCK_DGRAM)
    sock.settimeout(0.001)

    if isatty(stdin.fileno()):
        while True:
            data = stdin.readline()
            sock.sendto(data.encode(), address)

            try:
                data, address = sock.recvfrom(CHUNK)
                print(data)
            except TimeoutError:
                continue

    else:
        data = stdin.read()
        sock.sendto(data.encode(), address)

        print(f"[*] UDP packet sent to: {address}")

        print(f"[*] Sent {address}:")
        print(f" > {data.replace('\n', '\\n')}")

        try:
            data, address = sock.recvfrom(CHUNK)
            print(f"[*] Received {address}:")
            print(f" > {data}")
        except TimeoutError:
            print("[*] No response received")

    sock.close()
