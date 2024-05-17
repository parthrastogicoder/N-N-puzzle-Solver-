# A* Algorithm for n x n Puzzle Solving

## Introduction

This Python implementation leverages the A* algorithm to tackle the n x n sliding puzzle problem, a classic challenge in artificial intelligence and algorithmic problem-solving. The program is designed to efficiently solve square puzzles of arbitrary size by intelligently navigating the puzzle state space.

## Table of Contents
- [Overview](#overview)
- [Usage](#usage)
- [A* Algorithm](#a-algorithm)
- [Code Structure](#code-structure)
- [Example Application](#example-application)

## Overview

The project consists of three key components: a puzzle solver (`Solver` class), a puzzle representation (`Puzzle` class), and a node representation (`Node` class). These components collectively implement the A* algorithm to identify the optimal sequence of moves for solving an n x n puzzle.

## Usage

### Prerequisites
- Python installed on your system.

### Execution
1. Clone or download the code into a local directory.
2. Define an initial puzzle configuration using the `board` variable.
3. Verify the solvability of the puzzle with the `isSolvable` function.
4. Create a `Puzzle` object and a `Solver` object with the initial puzzle configuration.
5. Utilize the `solve` method of the `Solver` to obtain the solution.
6. Print the solution steps and any additional insights.

## A* Algorithm

The A* algorithm is a heuristic-based search algorithm widely used in pathfinding and graph traversal. It intelligently balances the actual cost to reach a state with a heuristic estimation of the cost to reach the goal. This implementation maintains a priority queue to efficiently explore states.

## Code Structure

### `Node` Class

- Represents a node in the search space.
- Stores information about the puzzle state, parent node, action taken, and cost.

### `Puzzle` Class

- Represents the n x n puzzle configuration.
- Provides methods for puzzle-solving logic, generating possible moves, calculating heuristics, and puzzle manipulation.

### `Solver` Class

- Implements the A* algorithm to find the optimal solution.
- Utilizes a priority queue to explore states in order of increasing cost.

## Example Application

```python
# Example of use
board = [[0, 3, 8], [4, 1, 7], [2, 6, 5]]
if isSolvable(board):
    print("The puzzle is solvable.")
else:
    print("The puzzle is not solvable. Please adjust the initial configuration.")
    exit()

puzzle = Puzzle(board)
solver = Solver(puzzle)
solution = solver.solve()

# Print solution steps
for node in solution:
    print(node.action)
    node.puzzle.pprint()

# Print additional information
print("Total number of steps in the solution: " + str(len(solution)))
