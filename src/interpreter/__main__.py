import argparse

from .scanner import Scanner

###############################################################################


def run(source: str) -> None:
    scanner = Scanner(source)


###############################################################################


def run_prompt() -> None:
    while True:
        print(">>> ", end="")
        try:
            line = input()
            run(line)
        except EOFError:
            print("Exiting...")
            break


###############################################################################


def run_file(path: str) -> None:
    with open(path, "r") as file:
        data = file.read()
        run(data)


###############################################################################


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=False, help="The file to run")
    return parser.parse_args()


###############################################################################


def main():
    args = parse_args()
    if args.file:
        run_file(args.file)
    else:
        run_prompt()


###############################################################################


if __name__ == "__main__":
    main()

###############################################################################
