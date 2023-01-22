# ___________________________________________________________________________ #


class ErrorHandler:
    """The ErrorHandler class"""

    had_error = False

    # ___________________________________________________________________________ #

    @staticmethod
    def error(line: int, message: str) -> None:
        ErrorHandler.report(line, "", message)

    # ___________________________________________________________________________ #

    @staticmethod
    def report(line: int, where: str, message: str) -> None:
        print(f"[line {line}] Error{where}: {message}")
        ErrorHandler.had_error = True

    # ___________________________________________________________________________ #


# ___________________________________________________________________________ #
