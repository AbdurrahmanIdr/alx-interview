# Pascal's Triangle Project

## Description

This project focuses on implementing a function to generate Pascal's Triangle in Python. Pascal's Triangle is a triangular array of numbers where each number is the sum of the two directly above it. This project aims to practice fundamental Python concepts such as lists, loops, functions, and arithmetic operations.

## Concepts Utilized

- **Lists and List Comprehensions**: Creating, accessing, modifying, and iterating over lists. Using list comprehensions for generating rows of Pascal's Triangle.
- **Functions**: Defining and calling functions, passing parameters, and returning values.
- **Loops**: Using nested loops to generate each row and calculate the values of Pascal's Triangle.
- **Conditional Statements**: Implementing logic based on the position within Pascal's Triangle.
- **Arithmetic Operations**: Performing addition to calculate each element of Pascal's Triangle.
- **Indexing and Slicing**: Accessing elements and slices of lists for constructing each row of the triangle.

## Requirements

- Python 3.4.3 or later
- All files should end with a new line
- The first line of all files should be `#!/usr/bin/python3`
- Include a `README.md` file
- Code should follow PEP 8 style guidelines

## Function Prototype

```python
def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal's triangle of n.
    Returns an empty list if n <= 0.
    """
```

## Output

```bash
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
```

## Project Structure

```bash
0x00-pascal_triangle/
├── 0-pascal_triangle.py  # Contains the `pascal_triangle` function
├── 0-main.py             # Test file to demonstrate the solution
└── README.md             # This README file
```
