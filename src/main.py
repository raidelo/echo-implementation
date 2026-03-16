from cli import argument_parser


def main() -> int:
    parser = argument_parser()
    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)

    else:
        parser.print_help()
        return 1

    return 0


if __name__ == "__main__":
    exit(main())
