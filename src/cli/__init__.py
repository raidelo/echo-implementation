from argparse import ArgumentParser

from ..client import process_client
from ..server import process_server


def argument_parser() -> ArgumentParser:
    parser = ArgumentParser()
    parser.add_argument("type", choices=["tcp", "udp"])

    subparser = parser.add_subparsers()

    pclient = subparser.add_parser("client")
    pclient.add_argument(
        "address",
        help="Specify the IP address or hostname to connect to.",
    )
    pclient.add_argument(
        "port",
        nargs="?",
        type=int,
        default=7,
        help="Specify the port number to use (default: 7).",
    )
    pclient.set_defaults(func=process_client)

    pserver = subparser.add_parser("server")
    pserver.add_argument(
        "--bind",
        default="0.0.0.0",
        help="Network interface to listen on (default: 0.0.0.0).",
    )
    pserver.add_argument(
        "port",
        nargs="?",
        type=int,
        default=7,
        help="Specify the port number to use (default: 7).",
    )
    pserver.set_defaults(func=process_server)

    return parser
