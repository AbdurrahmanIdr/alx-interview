#!/usr/bin/python3
"""UTF-8 validation module.
"""


def validUTF8(data):
    """
    Checks if a list of integers is valid UTF - 8.
    This is a helper function for L { parse_utf8 }.

    Args:
        data: A list of integers to check.
        The list must be sorted in ascending order of UTF - 8 codepoints.

    Returns:
        True if the list is valid False otherwise.
        Note that a list of integers is valid if and only 
        if they are in the range 0 < = i < 0x10ffff
    """
    skip = 0
    n = len(data)
    # skip is the number of bytes to skip
    for i in range(n):
        # Skips the next skip.
        if skip > 0:
            skip -= 1
            continue
        # skip 0 skip 1 skip 2 skip 3 skip 4 skip 3 skip 3 skip 2 skip
        # 3 skip 4 skip 3 skip 2 skip 3 skip 3 skip 2 skip 3 skip 3 skip
        # 2 skip 3 skip 3 skip 2 skip 3 skip 4 skip 2 skip 3 skip 2 skip 3
        # skip 2 skip 3 skip 3 skip 2 skip 3 skip 2 skip 3 skip 3 skip 2 skip
        # 3 skip 2 skip 3 skip 3 skip 2 skip 3 skip 3 skip 3 skip 3 skip 3 skip
        # 2 skip 3 skip 2 skip 3 skip 3 skip 3 skip 3 skip 3 skip 3 skip 3 skip
        # 2 skip 3 skip 4 skip 3 skip 4 skip 4 skip 4 skip 4 skip 4 skip
        if type(data[i]) != int or data[i] < 0 or data[i] > 0x10FFFF:
            return False
        elif data[i] <= 0x7F:
            skip = 0
        elif data[i] & 0b11111000 == 0b11110000:
            # 4-byte utf-8 character encoding
            span = 4
            # Check if the data is at the end of the data set.
            if n - i >= span:
                next_body = list(
                    map(
                        lambda x: x & 0b11000000 == 0b10000000,
                        data[i + 1: i + span],
                    )
                )
                # Return true if all body is empty.
                if not all(next_body):
                    return False
                skip = span - 1
            else:
                return False
        elif data[i] & 0b11110000 == 0b11100000:
            # 3-byte utf-8 character encoding
            span = 3
            # Check if the data is at the end of the data set.
            if n - i >= span:
                next_body = list(
                    map(
                        lambda x: x & 0b11000000 == 0b10000000,
                        data[i + 1: i + span],
                    )
                )
                # Return true if all body is empty.
                if not all(next_body):
                    return False
                skip = span - 1
            else:
                return False
        elif data[i] & 0b11100000 == 0b11000000:
            # 2-byte utf-8 character encoding
            span = 2
            # Check if the data is at the end of the data set.
            if n - i >= span:
                next_body = list(
                    map(
                        lambda x: x & 0b11000000 == 0b10000000,
                        data[i + 1: i + span],
                    )
                )
                # Return true if all body is empty.
                if not all(next_body):
                    return False
                skip = span - 1
            else:
                return False
        else:
            return False
    return True
