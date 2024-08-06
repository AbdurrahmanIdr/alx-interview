# 0x0A. Prime Game

## Description

This project involves developing an algorithm to determine the winner of a game based on the strategic removal of prime numbers and their multiples from a set of consecutive integers. The game is played between two players, Maria and Ben, where they take turns choosing a prime number from the set and removing that number and its multiples from the set. The player who cannot make a move loses the game.

## Concepts Covered

- Prime Numbers
- Sieve of Eratosthenes
- Game Theory
- Dynamic Programming / Memoization
- Python Programming

## Requirements

- Allowed editors: vi, vim, emacs
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A `README.md` file at the root of the project folder is mandatory
- Code should use the PEP 8 style (version 1.7.x)
- All files must be executable

## Tasks

### 0. Prime Game

**Task:** Maria and Ben are playing a game. Given a set of consecutive integers starting from 1 up to and including `n`, they take turns choosing a prime number from the set and removing that number and its multiples from the set. The player that cannot make a move loses the game.

- **Prototype:** `def isWinner(x, nums)`
  - `x` is the number of rounds
  - `nums` is an array of `n`
  - Return the name of the player that won the most rounds
  - If the winner cannot be determined, return `None`
  - You can assume `n` and `x` will not be larger than 10000
  - You cannot import any packages in this task

### Example

```python
x = 3
nums = [4, 5, 1]

# First round: 4
# Maria picks 2 and removes 2, 4, leaving 1, 3
# Ben picks 3 and removes 3, leaving 1
# Ben wins because there are no prime numbers left for Maria to choose

# Second round: 5
# Maria picks 2 and removes 2, 4, leaving 1, 3, 5
# Ben picks 3 and removes 3, leaving 1, 5
# Maria picks 5 and removes 5, leaving 1
# Maria wins because there are no prime numbers left for Ben to choose

# Third round: 1
# Ben wins because there are no prime numbers for Maria to choose

# Result: Ben has the most wins

print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3]))) # Winner: Ben
```

## Usage

```bash
./main_0.py
```

## Authors

- [Almeida Idris](https://github.com/AbdurrahmanIdr)
```