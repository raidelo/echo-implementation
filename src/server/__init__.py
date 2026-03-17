from argparse import Namespace
from socket import AddressFamily, SocketKind, socket
from threading import Thread
from typing import Generator


def process_server(args: Namespace) -> int:

    if args.type == "tcp":
        socket_stream((args.bind, args.port))

    elif args.type == "udp":
        socket_dgram((args.bind, args.port))

    else:
        return 1

    return 0


def socket_stream(address: tuple[str, int]) -> None:
    sock = socket(AddressFamily.AF_INET, SocketKind.SOCK_STREAM)

    sock.bind(address)

    sock.listen()

    print(f"[*] TCP Server listening at: {address}")

    pool = []

    while True:
        conn, address = sock.accept()
        th = Thread(target=handle_stream, args=(conn, address), daemon=True)
        th.start()
        pool.append(th)


def handle_stream(connection: socket, address: tuple[str, int]) -> None:
    print(f"[*] Connection established with: {address}")
    print("    Content:")

    for line in readlines(connection):
        print(f" > {line}")

        respond(connection, line)

    connection.close()


def readlines(connection: socket) -> Generator[bytes, None, None]:
    CHUNK = 64
    line = b""
    while True:
        received = connection.recv(CHUNK)
        if len(received) == 0:
            return
        line += received
        res = line.find(b"\n")
        if res != 0:
            y = line[: res + 1]
            line = line[res + 1 :]
            yield y


def respond(connection: socket, content: bytes) -> None:
    connection.sendall(content)


def socket_dgram(address: tuple[str, int]) -> None:
    sock = socket(AddressFamily.AF_INET, SocketKind.SOCK_DGRAM)

    raise NotImplementedError()
