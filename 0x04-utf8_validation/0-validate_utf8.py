#!/usr/bin/python3
"""UTF-8 validation module.
"""


def validUTF8(data):
    """
    Checks if a list of integers is valid UTF-8.

    Args:
        data: A list of integers to check.
            The list must be sorted in ascending order of UTF-8 codepoints.

    Returns:
        True if the list is valid, False otherwise.
        Note that a list of integers is valid if and only
        if they are in the range 0 <= i < 0x10FFFF.
    """
    skip = 0
    n = len(data)
    for i in range(n):
        if skip > 0:
            skip -= 1
            continue
        if not isinstance(data[i], int) or data[i] < 0 or data[i] > 0x10FFFF:
            return False
        elif data[i] <= 0x7F:
            skip = 0
        elif data[i] & 0b11111000 == 0b11110000:
            span = 4
            if n - i >= span:
                next_body = all(
                    (data[j] & 0b11000000) == 0b10000000
                    for j in range(i + 1, i + span)
                )
                if not next_body:
                    return False
                skip = span - 1
            else:
                return False
        elif data[i] & 0b11110000 == 0b11100000:
            span = 3
            if n - i >= span:
                next_body = all(
                    (data[j] & 0b11000000) == 0b10000000
                    for j in range(i + 1, i + span)
                )
                if not next_body:
                    return False
                skip = span - 1
            else:
                return False
        elif data[i] & 0b11100000 == 0b11000000:
            span = 2
            if n - i >= span:
                next_body = all(
                    (data[j] & 0b11000000) == 0b10000000
                    for j in range(i + 1, i + span)
                )
                if not next_body:
                    return False
                skip = span - 1
            else:
                return False
        else:
            return False
    return True
