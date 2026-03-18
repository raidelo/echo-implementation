from .cli import argument_parser


def _main() -> int:
    parser = argument_parser()
    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)

    else:
        parser.print_help()
        return 1

    return 0


def main() -> int:
    try:
        return _main()
    except KeyboardInterrupt:
        print("\n[*] Interrupt received ...")
        return 1


if __name__ == "__main__":
    main()
