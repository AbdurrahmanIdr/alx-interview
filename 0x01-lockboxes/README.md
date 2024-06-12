# Lockboxes Project

## Description

This project involves solving the "Lockboxes" problem, where you have `n` locked boxes, each potentially containing keys to other boxes. The goal is to determine if all boxes can be opened, starting with the first box (box 0) which is initially unlocked.

## Concepts Utilized

- **Lists and List Manipulation**: Understanding how to work with lists in Python.
- **Graph Theory Basics**: Utilizing Depth-First Search (DFS) to traverse through the boxes and keys.
- **Algorithmic Complexity**: Writing efficient algorithms with consideration of time and space complexity.
- **Recursion**: Implementing DFS, which can be done iteratively or recursively.
- **Queue and Stack**: Using stacks to manage the DFS traversal process.
- **Set Operations**: Keeping track of visited boxes using a set for optimal search performance.

## Requirements

- Python 3.4.3
- All files should end with a new line
- The first line of all files should be `#!/usr/bin/python3`
- Include a `README.md` file
- Code should follow PEP 8 style guidelines (version 1.7.x)
- All files must be executable

## Usage

To use the solution, you can run the provided `main_0.py` file, which tests the `canUnlockAll` function with different sets of boxes.

```bash
chmod +x main_0.py
./main_0.py
```

## Function Prototype

```python
def canUnlockAll(boxes):
    # boxes is a list of lists
    # A key with the same number as a box opens that box
    # Assume all keys will be positive integers
    # There can be keys that do not have boxes
    # The first box boxes[0] is unlocked
    # Return True if all boxes can be opened, else return False
```

## Example

```python
boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # True

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))  # True

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))  # False
```

## Project Structure

```bash
0x01-lockboxes/
├── 0-lockboxes.py  # Contains the `canUnlockAll` function
├── README.md       # This README file
└── main_0.py       # Test file to demonstrate the solution
```

## Author

[Abdurrahman Idris](https://github.com/AbdurrahmanIdr)

## License

This project is licensed under the [MIT License](../LICENCE).
