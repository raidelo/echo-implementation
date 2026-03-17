from socket import AddressFamily, SocketKind, socket

from .constants import CHUNK


def server_dgram(address: tuple[str, int]) -> None:
    sock = socket(AddressFamily.AF_INET, SocketKind.SOCK_DGRAM)

    sock.bind(address)

    print(f"[*] UDP Server listening at: {address}")

    while True:
        data, address = sock.recvfrom(CHUNK)
        handle_dgram(sock, data, address)


def handle_dgram(sock: socket, data: bytes, address: tuple[str, int]) -> None:
    print(f"[*] Data received from: {address}")
    print("    Content:")

    print(f" > {data}")

    respond_dgram(sock, address, data)


def respond_dgram(sock: socket, address: tuple[str, int], content: bytes) -> None:
    sock.sendto(content, address)
