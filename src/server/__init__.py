from argparse import Namespace

from .dgram import server_dgram
from .stream import server_stream


def process_server(args: Namespace) -> int:

    if args.type == "tcp":
        server_stream((args.bind, args.port))

    elif args.type == "udp":
        server_dgram((args.bind, args.port))

    else:
        return 1

    return 0
