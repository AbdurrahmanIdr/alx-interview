# Minimum Operations

This repository contains Python scripts that solve the "Minimum Operations" problem using dynamic programming techniques.

## Problem Description

Given a text file with a single character 'H', and two allowed operations, "Copy All" and "Paste", the task is to calculate the minimum number of operations required to achieve exactly `n` 'H' characters in the file.

### Tasks Overview

#### Task 0: Minimum Operations

**File:** `0-minoperations.py`

- **Description:** Implements a function `minOperations(n)` that calculates the fewest number of operations needed to achieve `n` 'H' characters.
- **Returns:** Returns an integer representing the minimum number of operations. If achieving `n` characters is impossible, it returns 0.

**Usage Example:**

```python
from 0-minoperations import minOperations

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
```

### Requirements

- Python version: 3.4.3
- Operating System: Ubuntu 20.04 LTS
- Editor: vi, vim, emacs

### Installation

Clone the repository and run the Python scripts using Python 3.4.3 in an Ubuntu 20.04 LTS environment.

```bash
git clone https://github.com/AbdurrahmanIdr/alx-interview.git
cd 0x02-minimum_operations
python3 -m venv venv
source venv/bin/activate
```

### License

This project is licensed under the [ALX License](../LICENCE) - see the LICENSE file for details.
