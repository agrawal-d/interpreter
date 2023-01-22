"""The interpreter module"""
from .scanner import Scanner

# ___________________________________________________________________________ #


class Interpreter:
    def run(self, source: str) -> None:
        scanner = Scanner(source)
        tokens = scanner.scan_tokens()

        for token in tokens:
            print(token)

    # ___________________________________________________________________________ #

    def run_file(self, path: str) -> None:
        try:
            with open(path, "r") as file:
                data = file.read()
                self.run(data)
        except FileNotFoundError:
            print(f"File not found: {path}")

    # ___________________________________________________________________________ #

    def run_repl(self) -> None:
        print("Lox interpreter (Python) (Ctrl+D to exit)")
        while True:
            print(">>> ", end="")
            try:
                line = input()
                self.run(line)
            except EOFError:
                print("Exiting...")
                break

    # ___________________________________________________________________________ #


# ___________________________________________________________________________ #
