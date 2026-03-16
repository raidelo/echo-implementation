from argparse import ArgumentParser

from client import process_client
from server import process_server


def argument_parser() -> ArgumentParser:
    parser = ArgumentParser()

    subparser = parser.add_subparsers()

    pclient = subparser.add_parser("client")
    pclient.add_argument(
        "address",
        help="Specify the IP address or hostname to connect to.",
    )
    pclient.add_argument(
        "port",
        nargs="?",
        default=7,
        help="Specify the port number to use (default: 7).",
    )
    pclient.set_defaults(func=process_client)

    pserver = subparser.add_parser("server")
    pserver.add_argument(
        "address",
        help="Specify the IP address or hostname to connect to.",
    )
    pserver.add_argument(
        "port",
        nargs="?",
        default=7,
        help="Specify the port number to use (default: 7).",
    )
    pserver.set_defaults(func=process_server)

    return parser
