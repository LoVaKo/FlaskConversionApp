import random
from enum import Enum


class ConversionType(Enum):
    BINARY_TO_DECIMAL = 0
    BINARY_TO_HEX = 1
    DECIMAL_TO_BINARY = 2
    DECIMAL_TO_HEX = 3
    HEX_TO_BINARY = 4
    HEX_TO_DECIMAL = 5


class Notation(Enum):
    BINARY = 0
    DECIMAL = 1
    HEXADECIMAL = 2
    

CONVERSION_MAP = {
    ConversionType.BINARY_TO_DECIMAL: {
        'original_notation': Notation.BINARY,
        'new_notation': Notation.DECIMAL
    },
    ConversionType.BINARY_TO_HEX: {
        'original_notation': Notation.BINARY,
        'new_notation': Notation.HEXADECIMAL
    },
    ConversionType.DECIMAL_TO_BINARY: {
        'original_notation': Notation.DECIMAL,
        'new_notation': Notation.BINARY
    },
    ConversionType.DECIMAL_TO_HEX: {
        'original_notation': Notation.DECIMAL,
        'new_notation': Notation.HEXADECIMAL,
    },
    ConversionType.HEX_TO_BINARY: {
        'original_notation': Notation.HEXADECIMAL,
        'new_notation': Notation.BINARY,
    },
    ConversionType.HEX_TO_DECIMAL: {
        'original_notation': Notation.HEXADECIMAL,
        'new_notation': Notation.DECIMAL,
    },
}


def random_number(notation):
    if notation == Notation.BINARY:
        length = random.randint(3, 10)
        return '1' + ''.join(random.choice('01') for _ in range(length - 1))  # Start with 1 to prevent leading zeroes

    if notation == Notation.DECIMAL:
        return random.randint(0, 500)

    if notation == Notation.HEXADECIMAL:
        length = random.randint(2, 4)
        hex_digits = '0123456789ABCDEF'
        return ''.join(random.choice(hex_digits) for _ in range(length))


def convert(original_notation, new_notation, original_value):
    if original_notation == Notation.BINARY:
        decimal_value = int(original_value, 2)
    elif original_notation == Notation.DECIMAL:
        decimal_value = int(original_value)
    elif original_notation == Notation.HEXADECIMAL:
        decimal_value = int(original_value, 16)
    else:
        raise ValueError("Original notation not recognized")

    if new_notation == Notation.BINARY:
        return bin(decimal_value)[2:]  # Strip 0b prefix
    elif new_notation == Notation.DECIMAL:
        return str(decimal_value)
    elif new_notation == Notation.HEXADECIMAL:
        return hex(decimal_value)[2:].upper()  # Strip 0x prefix
    else:
        raise ValueError("New notation not recognized")


def check(correct_answer, user_answer):
    return correct_answer == str(user_answer)


