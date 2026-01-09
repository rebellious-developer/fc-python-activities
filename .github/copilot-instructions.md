# Copilot Instructions for fc-python-activities

## Project Overview

This is a simple project created to demonstrate basic Python coding skills as part of a training/certification program with Future Connect. The focus is on showing to an instructor that I have learned basic Python programming.

## Project Structure

Currently minimal structure:
- [1-fizzbuzz.py](1-fizzbuzz.py) — Simple FizzBuzz implementation that prints 1..100 with Fizz/Buzz/FizzBuzz rules. Main entry: [`fizzbuzz`](1-fizzbuzz.py).
- [2-swap-string-case.py](2-swap-string-case.py) — Reads a string from the console and swaps letter case. Key function: [`str_swap_case`](2-swap-string-case.py).
- [3-swap-two-numbers.py](3-swap-two-numbers.py) — Demonstrates swapping two numbers using a third variable and without using a third variable. Key functions: [`swap_with_third_variable`](3-swap-two-numbers.py), [`swap_without_third_variable`](3-swap-two-numbers.py).
- [4-fibanacci-till-number.py](4-fibanacci-till-number.py) — Generates the Fibonacci series up to a user-entered limit (0..1,000,000). Key function: [`generate_fibonacci_series`](4-fibanacci-till-number.py).
- [5-number-guess-game.py](5-number-guess-game.py) — Console number guessing game (1..1000) with input validation and attempt limiting. Main entry: [`main`](5-number-guess-game.py).
- [6-basic-two-number-calculator.py](6-basic-two-number-calculator.py) — Minimal two-number calculator handling +, -, *, / with validation and division-by-zero handling. Key function: [`calculate`](6-basic-two-number-calculator.py) and entry: [`main`](6-basic-two-number-calculator.py).
- [README.md](README.md) — This file.
- [requirements.txt](requirements.txt) — Currently empty; no external dependencies required.
- [.python-version](.python-version) — Project Python version (3.12).
- [.gitignore](.gitignore) — Files and directories ignored by git.
- [.editorconfig](.editorconfig) — Editor configuration (PEP8 / indentation rules).
- [.github/copilot-instructions.md](.github/copilot-instructions.md) — Project Copilot usage guidance.


## Development Environment

### System Configuration
- **OS**: Ubuntu LTS
- **Version Control**: Git (latest via PPA)
- **SSH**: ed25519 key authentication for GitHub
- **CLI Tools**: GitHub CLI (gh) for repository management

### Git Configuration
- **Default branch**: `main`
- **Line endings**: LF (Unix-style) - configured globally with `core.eol lf`
- **Global ignore**: Uses `~/.git` ignore file for system-wide exclusions
- **Remote**: origin → `git@github.com:rebellious-developer/fc-python-activities.git`

## Key Workflows

### Creating New Python Files
When adding Python code to this project:
1. Create `.py` files in the root directory (no complex structure needed for training exercises)
2. Follow standard Python conventions (PEP 8)
3. Add executable permissions if creating scripts: `chmod +x filename.py`

### Git Workflow
Standard workflow used in this project:
```bash
git add <files>
git commit -m "descriptive message"
git push origin main
```

For new features, the project owner uses GitHub CLI for repo operations.

## Project Context

This is a **training/certification project** under the Future Connect organization:
- Focus on demonstrating basic Python development
- Additions should be educational and incrementally build skills
- Keep structure simple and beginner-friendly

## Python Guidelines

When adding Python code:
- Start with simple console applications (`print()` statements are fine)
- No frameworks or complex dependencies initially
- Add `requirements.txt` only when external packages are needed
- Use descriptive filenames that indicate the exercise purpose (e.g., `01_hello_world.py`, `02_variables.py`)

## Testing Approach

No formal testing framework currently configured. When adding tests:
- Use Python's built-in `unittest` or `pytest` for simplicity
- Create a `tests/` directory when needed
- Document test execution in README.md
