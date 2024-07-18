# UTF-8 Validation

This repository contains a solution to the UTF-8 validation problem. The task is to determine if a given data set represents a valid UTF-8 encoding. This involves applying knowledge of bitwise operations, understanding the UTF-8 encoding scheme, and utilizing Python programming skills.

## Requirements

- All files are interpreted/compiled on Ubuntu 20.04 LTS using Python 3 (version 3.4.3).
- All files end with a new line.
- The first line of all files is exactly `#!/usr/bin/python3`.
- Code adheres to the PEP 8 style (version 1.7.x).
- All files are executable.

## Project Structure

- `0-validate_utf8.py`: Contains the `validUTF8` function which checks if a list of integers is a valid UTF-8 encoding.
- `0-main.py`: Main file for testing the `validUTF8` function.
- `README.md`: Project description and documentation.

## Usage

To test the `validUTF8` function, run the `0-main.py` file:

```bash
./0-main.py
```

## Function Description

### `validUTF8(data)`

- **Args:**
  - `data`: A list of integers representing the data to check. Each integer represents 1 byte of data, and only the 8 least significant bits are considered.
- **Returns:**
  - `True` if the data is a valid UTF-8 encoding, otherwise `False`.

## Example

```python
validUTF8 = __import__('0-validate_utf8').validUTF8

data1 = [65]
print(validUTF8(data1))  # True

data2 = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data2))  # True

data3 = [229, 65, 127, 256]
print(validUTF8(data3))  # False
```

## Concepts Needed

- **Bitwise Operations in Python:** Understanding how to manipulate bits in Python, including operations like AND (`&`), OR (`|`), XOR (`^`), NOT (`~`), shifts (`<<`, `>>`).
  - [Python Bitwise Operators](https://realpython.com/python-bitwise-operators/)
- **UTF-8 Encoding Scheme:** Familiarity with the UTF-8 encoding rules, including how characters are encoded into one or more bytes.
  - [UTF-8 Wikipedia](https://en.wikipedia.org/wiki/UTF-8)
  - [Characters, Symbols, and the Unicode Miracle](https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/)
- **Data Representation:** How to represent and work with data at the byte level.
- **List Manipulation in Python:** Iterating through lists, accessing list elements, and understanding list comprehensions.
  - [Python Lists](https://docs.python.org/3/tutorial/datastructures.html)
- **Boolean Logic:** Applying logical operations to make decisions within the program.

## Additional Resources

- [Mock Technical Interview](https://www.mocktechnicalinterview.com)

## License

This project is licensed under the MIT License - see the [LICENSE](../LICENCE) file for details.
