Markdown
# Recursive Maze Generator & DFS Solver

A Python command-line utility that procedurally generates text-based mazes and solves them using recursive backtracking. 

## Project Motivation & Constraints
This project was built as a zero-dependency challenge to explore foundational data structures and graph traversal from first principles. Rather than relying on external libraries like `numpy` for matrix management, the architecture intentionally uses a custom `Grid` class to manually handle boundary validation, deep-copying, and 2D state management. 

## Features
*   **Procedural Generation:** Generates unique, solvable maze matrices of dynamic dimensions using a randomized recursive carving algorithm.
*   **DFS Pathfinding:** Solves provided mazes by exhaustively searching viable paths, leaving a breadcrumb trail (`.`), and efficiently backtracking out of dead ends.
*   **Custom State Management:** Uses a dedicated `Grid` object to securely abstract 2D array manipulation and coordinate indexing.
*   **CLI Routing:** Fully operable via the command line with dedicated flags for generation and solving logic.

## Usage

**Generate a Maze**
Generates a new maze of specified width and height, saving it to a text file.
*(Note: Dimensions must be at least 3x5. Even numbers are automatically rounded up to maintain structural walls).*

```bash
python main.py -g <width> <height> <output_filename.txt>
```

**Solve a Maze**
Reads a maze from a text file, locates the start (`S`), and prints the mapped path to the exit (`E`) to the console.

```bash
python main.py -s <input_filename.txt>
```

## Architecture & State Management
The engine relies on modifying 2D arrays in-place to manage state.

*   **The Grid Class (`Grid.py`):** Acts as the core data structure, handling boundary validation, strict matrix formatting requirements, and deep-copying states to ensure memory independence during complex transformations.

*   **The Recursive Stack:** During the pathfinding routine, the algorithm tracks explored vectors to prevent infinite loops and unwinds the recursive stack to reset state parameters upon hitting a dead end.
