import argparse

from .errorHandler import ErrorHandler
from .interpreter import Interpreter

# ___________________________________________________________________________ #


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=False, help="The file to run")
    return parser.parse_args()


# ___________________________________________________________________________ #


def main() -> None:
    args = parse_args()
    interpreter = Interpreter()

    if args.file:
        interpreter.run_file(args.file)
    else:
        interpreter.run_repl()

    if ErrorHandler.had_error:
        exit(65)


# ___________________________________________________________________________ #


if __name__ == "__main__":
    main()

# ___________________________________________________________________________ #
