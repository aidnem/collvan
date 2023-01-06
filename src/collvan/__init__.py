import argparse
from sys import argv
from typing import Callable

def run_console():
    """Entry point when collvan is run from the console `collvan ...`"""
    main()

"""List of collvan tool names, and their respective main functions"""
COLLVAN_TOOLS: dict[str, Callable[[list[str]], None]] = {
}

def parse_args(args: list[str]) -> argparse.Namespace:
    """Parse commandline arguments passed to script"""
    parser = argparse.ArgumentParser(
        prog = "collvan",
        description = "a suite of tools to make writing Collver programs easier",
        epilog = "the `collvan` command is a wrapper around all of Collvan's tools",
    )

    parser.add_argument(
        "tool",
        metavar="tool",
        choices=COLLVAN_TOOLS,
        help="Name of tool in the Collvan suite to be run. Allowed values are: " + ", ".join(COLLVAN_TOOLS),
    )

    parser.add_argument(
        "toolargs",
        metavar="arguments",
        nargs=argparse.REMAINDER,
        help="All arguments after the `tool` argument are passed to the sub-tool specified"
    )

    return parser.parse_args(args)

def main():
    args: argparse.Namespace = parse_args(argv)
    print(f"[collvan wrapper] running tool '{args.tool}' with args {args.toolargs}")
    COLLVAN_TOOLS[args.tool](args.toolargs)
