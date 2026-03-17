from argparse import Namespace

from .dgram import client_dgram
from .stream import client_stream


def process_client(args: Namespace) -> int:

    if args.type == "tcp":
        client_stream((args.address, args.port))

    elif args.type == "udp":
        client_dgram((args.address, args.port))

    else:
        return 1

    return 0
