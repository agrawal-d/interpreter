"""Scanning utilities"""
from enum import Enum, auto
from typing import List

from .errorHandler import ErrorHandler

# ___________________________________________________________________________ #


class TokenType(Enum):
    # Single char tokens
    LEFT_PAREN = auto()
    RIGHT_PAREN = auto()
    LEFT_BRACE = auto()
    RIGHT_BRACE = auto()
    COMMA = auto()
    DOT = auto()
    MINUS = auto()
    PLUS = auto()
    SEMICOLON = auto()
    SLASH = auto()
    STAR = auto()

    # One or two char tokens
    BANG = auto()
    BANG_EQUAL = auto()
    EQUAL = auto()
    EQUAL_EQUAL = auto()
    GREATER = auto()
    GREATER_EQUAL = auto()
    LESS = auto()
    LESS_EQUAL = auto()

    # Literals
    IDENTIFIER = auto()
    STRING = auto()
    NUMBER = auto()

    # Keywords
    AND = auto()
    CLASS = auto()
    ELSE = auto()
    FALSE = auto()
    FUN = auto()
    FOR = auto()
    IF = auto()
    NIL = auto()
    OR = auto()
    PRINT = auto()
    RETURN = auto()
    SUPER = auto()
    THIS = auto()
    TRUE = auto()
    VAR = auto()
    WHILE = auto()

    EOF = auto()


# ___________________________________________________________________________ #


class Tokens:
    token_type: TokenType
    lexeme: str
    literal: object
    line: int

    # ___________________________________________________________________________ #

    def __init__(
        self, token_type: TokenType, lexeme: str, literal: object, line: int
    ) -> None:
        self.token_type = token_type
        self.lexeme = lexeme
        self.literal = literal
        self.line = line

    # ___________________________________________________________________________ #

    def __str__(self) -> str:
        return f"{self.token_type} {self.lexeme} {self.literal}"

    # ___________________________________________________________________________ #


# ___________________________________________________________________________ #


class Scanner:
    source: str = ""
    tokens: List[Tokens]
    start: int
    current: int
    line: int

    # ___________________________________________________________________________ #

    def __init__(self, source: str) -> None:
        self.source = source
        self.tokens = []
        self.start = 0
        self.current = 0
        self.line = 1

    # ___________________________________________________________________________ #

    def is_at_end(self) -> bool:
        return self.current >= len(self.source)

    # ___________________________________________________________________________ #

    def advance(self) -> str:
        character = self.source[self.current]
        self.current += 1
        return character

    # ___________________________________________________________________________ #

    def add_token(self, token_type: TokenType, literal: object = None) -> None:
        text = self.source[self.start : self.current]
        self.tokens.append(Tokens(token_type, text, literal, self.line))

    def match(self, expected: str) -> bool:
        if self.is_at_end():
            return False

        if self.source[self.current] != expected:
            return False

        self.current += 1
        return True

    # ___________________________________________________________________________ #

    def scan_token(self) -> None:
        char = self.advance()

        if char == "(":
            self.add_token(TokenType.LEFT_PAREN)
        elif char == ")":
            self.add_token(TokenType.RIGHT_PAREN)

        elif char == "{":
            self.add_token(TokenType.LEFT_BRACE)

        elif char == "}":
            self.add_token(TokenType.RIGHT_BRACE)

        elif char == ",":
            self.add_token(TokenType.COMMA)

        elif char == ".":
            self.add_token(TokenType.DOT)

        elif char == "-":
            self.add_token(TokenType.MINUS)

        elif char == "+":
            self.add_token(TokenType.PLUS)

        elif char == ";":
            self.add_token(TokenType.SEMICOLON)

        elif char == "*":
            self.add_token(TokenType.STAR)

        elif char == "!":
            if self.match("="):
                self.add_token(TokenType.BANG_EQUAL)
            else:
                self.add_token(TokenType.BANG)
        elif char == "=":
            if self.match("="):
                self.add_token(TokenType.EQUAL_EQUAL)
            else:
                self.add_token(TokenType.EQUAL)
        elif char == "<":
            if self.match("="):
                self.add_token(TokenType.LESS_EQUAL)
            else:
                self.add_token(TokenType.LESS)
        elif char == ">":
            if self.match("="):
                self.add_token(TokenType.GREATER_EQUAL)
            else:
                self.add_token(TokenType.GREATER)
        else:
            ErrorHandler.error(self.line, f"Unexpected character. {char}")

    # ___________________________________________________________________________ #

    def scan_tokens(self) -> List[Tokens]:
        while not self.is_at_end():
            self.start = self.current
            self.scan_token()

        self.tokens.append(Tokens(TokenType.EOF, "", None, self.line))
        return self.tokens

    # ___________________________________________________________________________ #


# ___________________________________________________________________________ #
